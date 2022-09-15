# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class matrix__telecoms__sms(models.Model):
     _name = 'matrix__telecoms__sms.vt'
     
     nom = fields.Char("Typer la visite")
     client_id = fields.Many2one(
          'res.partner',
          string='Client visité',
          )
     start_date = fields.Date(default=fields.Date.today)
     duration = fields.Float(digits=(6, 2), help="Durée en jours")
     
     end_date = fields.Date(string="Date de fin", store=True,
        compute='_get_end_date', inverse='_set_end_date')
     
     @api.depends('start_date', 'duration')
     def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration

     def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1
     

    
