# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Staff(models.Model):
    _name = "staff"
    _description = "Staff model"

    name = fields.Char('Name Staff', required=True)
    age = fields.Float('age')

    task_ids = fields.Many2many('task', string="Task")

