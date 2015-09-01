# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    heading = fields.Many2one(comodel_name='crm.heading')
