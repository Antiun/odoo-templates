# -*- coding: utf-8 -*-
# License AGPL-3: Antiun Ingenieria S.L. - Antonio Espinosa
# See README.rst file on addon root folder for more details

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    heading = fields.Many2one(comodel_name='crm.heading')
