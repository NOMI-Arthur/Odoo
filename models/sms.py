# -*- coding: utf-8 -*-
from odoo import fields, models
import os

class SMSforClients(models.Model):
    _name = 'matrix__telecoms__sms.sms'

    recepteur = fields.Char(string='Recepteur', Required=True, default="2376")
    expediteur = fields.Char(string='Expéditeur', default="MatrixTelec", readonly=True)
    message = fields.Text("Votre message", Required=True, default="Le message à saisir ici...")
    receiveur = recepteur

    def callSender(self):
        os.system("python msg.py")
    
    def saveData(self):
        with open("phone.txt", 'w') as fa:
            sender = "Matrix Télécoms RNOC"
            text = "Vous avez a envoyé un message au "
            text = text.upper()
            fa.write(text)