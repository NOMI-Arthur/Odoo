# -*- coding: utf-8 -*-
import string
from odoo import fields, models, api

class ticket(models.Model):
    _name = 'matrix__telecoms__sms.ticket'
    
    code = fields.Char("Mon soucis")
    descriptionTicket = fields.Text(string="Description", default="Description du Ticket")
    proprietaire_id = fields.Many2one(
        'res.partner',
        string='Propriétaire du code',
        )
    etat = fields.Selection([('ouvert', 'ouvert'),('plan', 'plannifié'),('encours', 'En cours'),('appro', 'En attente approbation'),('fermer', 'Fermer')])