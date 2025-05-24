"""
Définition des champs de sur la BD de peef.dev et res.partner
Les champs avec (+) ont été ajouté et ne sont pas présents dans res.partner tels quels

linkedin = linkedin (+char|widget website)
is_available = is_available (+boolean)
sex = sex (+selection)
skills = skills (+char)
spoken_languages = spoken_languages (+char)
is_freelance = is_freelance (+Boolean)
user_type = user_type (+selection)
onboard_step = onboard_step (+selection)
title = description (+char)
referral_code = referral_code (+char)
discount = discount (+float)
points = points (+integer)
daily_rate = daily_rate (+monetary)

username = ref
email = email
active = active
phone = phone
bio = notes
location = city
website = website
full_name = name
"""

from odoo import models, fields, api


class PeefPartner(models.Model):
    _inherit = 'res.partner'

    is_available = fields.Boolean(string="Available")
    linkedin = fields.Char(string="LinkedIn")
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Sex")
    skills = fields.Char(string="Skills")
    spoken_languages = fields.Char(string="Spoken languages")
    is_freelance = fields.Boolean(string="Is freelance")
    user_type = fields.Selection([
        ('creator', 'Expert'),
        ('need_service', 'Entreprise'),
        ('nothing', 'Nothing'),
        ('admin', 'Administrator'),
        ('system', 'System'),
    ], string="User Type")
    onboard_step = fields.Selection([
        ('start', 'Registration'),
        ('basics', 'Basic profil information'),
        ('expertise', 'Competences or specific needs'),
        ('complete', 'Profil complete'),
    ], string="Onboarding step")
    professional_title = fields.Char(string="Professional title")
    referral_code = fields.Char(string="Referral code")
    discount = fields.Float(string="Discount")
    points = fields.Integer(string="Credits")
    daily_rate = fields.Float(string="Daily rate")

    # for record in records:
    #     opportunity_name = record.mapped("category_id.name")
    #     current_opportunity = env["crm.lead"].search([("name", "in", opportunity_name), ("partner_id", "=", record.id)])
    #     existing_crm_tags = env["crm.lead"].search_read([], ["name"])
    #
    #     if not current_opportunity:
    #
    #         tag_ids = []
    #         for name in opportunity_name:
    #             tag = env["crm.tag"].search([("name", "=", name)], limit=1)
    #             if tag:
    #                 tag_ids.append(Command.link(tag.id))
    #             else:
    #                 tag_ids.append(Command.create({"name": name}))
    #
    #         env["crm.lead"].create({
    #             "partner_id": record.id,
    #             # always take the first tag for the current opportunity
    #             "name": opportunity_name[0],
    #             "stage_id": env.ref("crm.stage_lead1").id,
    #             "email_from": record.email,
    #             "phone": record.phone,
    #             "tag_ids": tag_ids
    #         })
