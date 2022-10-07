# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Task(models.Model):
    _name = "task"
    _description = "Task model"

    name = fields.Char('Name Task', required=True)

    project_id = fields.Many2one('project1', string='Project')
    staff_id = fields.Many2one('staff', string='Staff')

    # staff_ids = fields.One2many('staff', 'task_id', string='Staff')


