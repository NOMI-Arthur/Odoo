# -*- coding: utf-8 -*-
from odoo import fields, models, api

class contacts(models.Model):
    _name = 'matrix__telecoms__sms.message'
    
    sender = fields.Char(string="Expéditeur", required=True, default="MATRIX Télé")
    receiver_user = fields.Many2one(
        'res.users',
        string="Envoyer à l'employé",
        required=True,
        )
    receiver_partner = fields.Many2one(
        'res.partner',
        string="Envoyer au client",
        )
    receiver = fields.Char(string="Numéro", required=True, default="saisir le numero ici...")
    message = fields.Text(string="Corps du message", required=True, default="Ici le corps du message")
    
 
        