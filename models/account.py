# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api

class account(models.Model):
     _name = 'matrix__telecoms__sms.account'
     
     montant = fields.Float("Versement mensuel")
     mouvement = fields.Float("Charge du jour")   
     compte_ids = fields.Many2many('matrix__telecoms__sms.compte', string="Compte")
       

    
