# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Task(models.Model):
    _name = "task1"
    _description = "Task model"

    name = fields.Char('Name Task', required=True)
    dateLine = fields.Date('Date Line')
    status = fields.Char('Status', default='ToDo')

    staff_id = fields.Many2one('res.users', string="Manager")   #Manager
    staff_ids = fields.Many2one('res.users', string="Assign to", default=lambda self: self.env.user)   #Assign to

    # staff_ids = fields.Many2many('res.users', string='Assign to', default=lambda self: self.env.user)   #Assign to

