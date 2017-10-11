from odoo import models, fields , api

class isic_codes(models.Model):
   _name = "is.isic.codes"
   code = fields.Char(string="code", required=True)



 












