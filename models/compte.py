# -*- coding: utf-8 -*-

from odoo import models, fields, api

class matrix__telecoms__sms(models.Model):
     _name = 'matrix__telecoms__sms.compte'
     
     proprietaire_id = fields.Many2one(
          'res.partner',
          string='Client Propriétaire',
          )
     typeCompte = fields.Selection([('currentAccount', 'compte client'), ('partAccount', 'Compte Partenaire'), ('empAccount', 'compte employé')])

    
