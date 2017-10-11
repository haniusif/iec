from odoo import models, fields , api

class investors(models.Model):
   _name = "is.investors"
   name = fields.Char(string="investor name", required=True)
   phone = fields.Integer()




 












