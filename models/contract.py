# -*- coding: utf-8 -*-

from odoo import models, fields, api

class matrix__telecoms__sms(models.Model):
     _name = 'matrix__telecoms__sms.contract'
     
     nomClient_id = fields.Many2one(
        'res.partner',
        string='Client Contract',
        default='pour le client',
        )
     employeCocontractant_id = fields.Many2one(
        'res.users',
        string='Employé co-contractant',
        default="Avec l'employé",
        )
     termes = fields.Text("Termes du contract", default="Termes du contract")
     
     
     

    
