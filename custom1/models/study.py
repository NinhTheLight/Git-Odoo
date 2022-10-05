# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Study(models.Model):
    _name = "study"
    _description = "Study model"

# Tuan1
    # name = fields.Char('Name', required=True)
    # age = fields.Integer('Age', default=1)
    # dateBirth = fields.Date('Birth', required=True)
    # weight = fields.Float('Weight (kg)', digits=(2, 4))
    # height = fields.Float('Height (m)')
    #
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female')
    # ], string='Gender', default='male')
    # note = fields.Text('Note')
    #
    # image = fields.Binary("Pet Image", attachment=True, help="Pet Image")
    #
    # testField = fields.Char("testField", size=8, trim=True, translate=True)

# Tuan2
    name = fields.Char('Name', required=True)
    assign = fields.Many2one('res.users', string="Assign")
    dateLine = fields.Date('Date Line')
    status = fields.Selection([
        ('todo', 'ToDo'),
        ('progress', 'Progress'),
        ('review', 'Review'),
        ('done', 'Done')
    ])
    description = fields.Html('Description')
