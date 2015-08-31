# -*- coding: utf-8 -*-
##############################################################################
# License AGPL-3 - See LICENSE file on repo root folder for details
##############################################################################

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    heading = fields.Many2one(comodel_name='crm.heading')
