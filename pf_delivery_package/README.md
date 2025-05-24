# Delivery package

A module for optimizing delivery packaging.

The product dimension depends on product_dimension from OCA

When the module is installed, packaging options are automatically activated

Odoo already handles by default the case of choosing the appropriate package based on the product quantity
It means that after packaging option is activated,
If we have a product of quantity 8 that has a configured package with quantity 8, that package will be choosen.


## Gloabal idea

The package types and packages are linked to products (it will be the package product)

The picking is linked to a default package type

When we create a picking, we should specify the default package type of that picking

Then, when we Put in pack, the default picking type in that picking is used to check the product

When the package is created, a new move line with the package product that is linked to the package type is created

We can then have a picking with 2 products (the main product and the package product)

## Usage

- Create 2 products : one normal product for example "Book" and a package product for example "Carton"

- For the product Book, you can link a packaging in the tab Inventory

- Go to inventory -> Configuration -> Package type and create a package type with the product Carton linked to it

- Create now a delivery and choose a default package type (the field is mandatory)

- Mark as to do, put in pack (the package product is linked to it)
