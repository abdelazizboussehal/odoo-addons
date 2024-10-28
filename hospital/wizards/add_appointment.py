from odoo import models, fields, api


class AddAppointments(models.TransientModel):
    _name = 'add.appointment'

    name = fields.Char(compute='_compute_header_name')
    patient_id = fields.Many2one('res.partner', string='Patient', required=True, domain="[('isPatient', '=', True)]")
    notes = fields.Text(string='Notes')
    app_date = fields.Datetime(string='Date Time', required=True)
    doctor_id = fields.Many2one('res.users', 'Doctor', domain="[('isDoctor', '=', True)]")

    @api.depends('patient_id')
    def _compute_name(self):
        print('Trigger from add appointment')
        for record in self:
            record.name = f"Adding an appointment for {record.patient_id.name}"

    def confirm_appointment(self):
        print('ok')
