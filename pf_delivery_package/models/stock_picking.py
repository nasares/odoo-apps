from odoo import models, fields, api, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    default_package_type_id = fields.Many2one(
        'stock.package.type',
        string="Default Package Type",
        required=True,
        help="Default package type to use when putting items in a package for this picking."
    )

    def _create_package_product_move(self, package, product):
        """
        Create a stock move and move line for a package product

        Args:
            package: stock.quant.package record
            product: product.product record for the package

        Returns:
            stock.move: The created move
        """
        existing_move = self.move_ids.filtered(
            lambda m: m.product_id.id == product.id
        )

        if existing_move:
            return existing_move

        vals = {
            'name': product.name,
            'product_id': product.id,
            'product_uom': product.uom_id.id,
            'product_uom_qty': 1,
            'picking_id': self.id,
            'location_id': self.location_id.id,
            'location_dest_id': self.location_dest_id.id,
            'state': 'draft',
            # to avoid reservation issues, additional = True
            'additional': True,
            'description_picking': _("Package: %s") % package.package_type_id.name,
        }

        new_move = self.env['stock.move'].create(vals)

        new_move._action_confirm()
        new_move._action_assign()

        move_line_vals = {
            'product_id': product.id,
            'product_uom_id': product.uom_id.id,
            'quantity': 1,  # Always set to 1
            'picking_id': self.id,
            'location_id': self.location_id.id,
            'location_dest_id': self.location_dest_id.id,
            'move_id': new_move.id,
            'package_id': False,
            'result_package_id': package.id,
        }

        self.env['stock.move.line'].create(move_line_vals)

        return new_move

    def _put_in_pack(self, move_line_ids):
        package = super(StockPicking, self)._put_in_pack(move_line_ids)

        package_type = package.package_type_id or self.default_package_type_id

        if package_type and not package.package_type_id:
            package.write({'package_type_id': package_type.id})

        if package_type and package_type.product_id:
            package_product = package_type.product_id

            package.sudo().write({'product_id': package_product.id})

            self._create_package_product_move(package, package_product)

        return package