from odoo import models, fields , api

class requests(models.Model):
	_name = "is.requests"
	investor_id = fields.Many2one('is.investors', string="investor name" , required=True)
	investor_name = fields.Char(related ="investor_id.name")
	investor_phone = fields.Integer(related="investor_id.phone")
	investor_address = fields.Char()
	lStatus = fields.Selection(selection=[('owner', 'owner'),('agent', 'agent')] , default='owner')
	inv_type = fields.Selection(selection=[('patriotic', 'patriotic'),('Foreigner', 'Foreigner'),('Mutual', 'Mutual')] , default='patriotic')
	sector = fields.Selection(selection=[('agricultural', 'agricultural'),('Artificial', 'Artificial'),('service', 'service')] )
	investor_gender = fields.Selection(selection=[('male', 'Male'),('female', 'Female')])
	isic_codes = fields.Many2one('is.isic.codes', string="isic codes" , required=True)
	investor_email = fields.Char()
	company_img = fields.Binary()
	isic_desc = fields.Text()
	worker = fields.Integer()
	capital = fields.Integer()
	work_l_status = fields.Selection(selection=[('company', 'company'),('individual', 'individual'),('copartnership', 'copartnership')] , default='individual')


   




 












