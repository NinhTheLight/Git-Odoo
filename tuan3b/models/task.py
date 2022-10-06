# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Task(models.Model):
    _name = "task"
    _description = "Task model"

    name = fields.Char('Name Task', required=True)
    dateLine = fields.Date('Date Line')

    staff_id = fields.Many2one('staff', string="Manager")
    staff_ids = fields.Many2many('staff', String='Staff')

    # user_ids = fields.Many2many('res.users', string='User')
    # task_ids = fields.Many2many('res.partner', string='Task')

    # user_ids = fields.One2many('user', 'project_id', string="Attendees")
