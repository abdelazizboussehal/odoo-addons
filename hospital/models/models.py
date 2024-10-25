# -*- coding: utf-8 -*-
from datetime import date

from odoo import models, fields, api


# from odoo import models, fields, api


# class hospital(models.Model):
#     _name = 'hospital.hospital'
#     _description = 'hospital.hospital'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Patient(models.Model):
    _inherit = 'res.partner'
    isPatient = fields.Boolean(default=False, string='Is Patient?')
    dateOfBirth = fields.Date(string='date of birth')
    age = fields.Integer(string='Age')
    appointment = fields.One2many('hospital.appointment', 'patient_id', string='Appointment List')
    doctor_id = fields.Many2one('res.users', string='Doctor')
    appointment_count = fields.Integer(string='Appointment Count', default='0', compute='_compute_appointment_count')


    @api.model
    @api.onchange('dateOfBirth')
    def onchange_dateOfBirth(self):
        today = date.today()
        if self.dateOfBirth:
            self.age = today.year - self.dateOfBirth.year

    @api.depends('appointment')
    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = len(record.appointment)

    def action_patient_list_of_appointments(self):
        ctx = dict(
            patient_id=self.id,
        )
        return {
            'name': 'Appointments Obj',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
            'res_model': 'hospital.appointment',
            'type': 'ir.actions.act_window',
            'context': ctx
        }


class Doctor(models.Model):
    _inherit = 'res.users'
    isDoctor = fields.Boolean(default=False, string='Is a Doctor')
    isSupervisor = fields.Boolean(default=False, string='Is a Supervisor')
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments List')
    patient_ids = fields.One2many('res.partner', 'doctor_id', string='Patients List')
