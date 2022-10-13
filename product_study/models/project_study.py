# -*- coding: utf-8 -*-
from datetime import datetime

from stdnum.at import uid

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
class Project(models.Model):
    _name = "project.study"
    _description = "Project study model"
    _inherit = ['mail.thread']
    # _inherit = ['mail.thread', 'ir.need-action_mixin']
    # _inherit = ['mail.thread', 'ir.need_action_mixin']
    _inherit = ['mail.thread', 'mail.activity.mixin']



    name = fields.Char('Name', required=True)
    dateline = fields.Date('DateLine', required=True)
    start_date = fields.Date('StartDate')
    end_date = fields.Date('EndDate')
    description = fields.Html('Description')

    status = fields.Selection([
        ('todo', 'ToDo'),
        ('in-progress', 'In-progress'),
        ('review', 'Review'),
        ('done', 'Done'),
    ], default='todo', tracking=True)

    tags = fields.Selection([
        ('bug', 'Bug'),
        ('newfeature', 'New feature'),
        ('done', 'Done'),
    ])

    manager = fields.Many2many('res.users', string="Manager")
    staff_id = fields.One2many('res.users', 'project_id', string='Assign to', default=lambda self: self.env.user)
    customer_id = fields.Many2one('res.partner', string='Customer')

    assigned_update_at = fields.Datetime('Assigned update at', compute="_compute_update_date_assign", store=True)

    # message_follower_ids = fields.Char(string='Log message')
    # manager_link_user = fields.Many2one('res.users')
    # task_ids = fields.One2many('task3', 'project_id', string="Tasks")
    # staff_id_in_task = fields.Many2many('res.users', string="staff_id_in_task")
    # staff_id_in_task = fields.One2many('task3', 'staff_id', string="staff_id_in_task")

    @api.constrains('customer_id')
    def _check_customer_exist(self):
        for item in self:
            if item.customer_id.id != False:
                condition = self.env['project.study'].search([('customer_id', '=', item.customer_id.id), ('id', '!=', item.id)])
                if condition:
                    raise ValidationError("Customer " +item.customer_id.name+ " already exist in other task.  Please choose another customer")

    @api.depends("staff_id.name")
    def _compute_update_date_assign(self):
        for record in self:
            record.assigned_update_at = datetime.today().now()

    @api.onchange("staff_id")
    def _onchange_assignto(self):
        self.tags = 'newfeature'


class AddInformationUsers(models.Model):
    _inherit = "res.users"

    project_id = fields.Many2one('project.study')

    # user_link_project = fields.One2many('project.study', 'manager')
    position = fields.Char('Position')
    # a = fields.Char(string='phan tram')

    # def action_position(self):
    #     for record in self:
    #         condition = self.env['project.study'].search(
    #             [('manager', '=', uid)])
    #         if condition:
    #             record.write({'position': 'manager'})
    #         else:
    #             record.write({'position': 'staff'})

