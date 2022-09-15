# -*- coding: utf-8 -*-
from odoo import fields, models

class ClientMT(models.Model):
    _inherit = 'res.partner'
    
    #codepromo_id = fields.Many2one('matrix__telecoms__sms.ticket', string='Code Promo', ondelete='set null',)