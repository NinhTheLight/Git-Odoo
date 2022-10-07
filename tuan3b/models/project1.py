# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class Project(models.Model):
    _name = "project1"
    _description = "Project model"

    name = fields.Char('Name Project', required=True)
    dateLine = fields.Date('Date Line')
    status = fields.Char('Status', default='ToDo')

    manager = fields.Many2one('staff', string="Manager")
    task_ids = fields.One2many('task', 'project_id', string="Tasks")


    # staff_ids = fields.Many2many('staff', String="Assign to")   #Assign to
    # staff_ids = fields.Many2many('res.users', 'Current User', default=lambda self: self.env.user)
    # staff_ids = fields.Many2one('res.users', string='Current User', default=lambda self: self.env.user )   #Manager
    # user_ids = fields.Many2many('res.users', string='User')
    # task_ids = fields.Many2many('res.partner', string='Task')
    # user_ids = fields.One2many('user', 'project_id', string="Attendees")
