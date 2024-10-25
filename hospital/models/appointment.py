from odoo import fields, models, api


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Description'

    dateAppointment = fields.Date(string='Appointment Date', required=True)
    patient_id = fields.Many2one('res.partner', string='patient',
                                 default=lambda self: self.env.context.get('patient_id'))
    # IMPORTANT::
    doctor_id = fields.Many2one('res.users', string='Doctor', default=lambda self: self.env.user.id)
    dateOfBirth = fields.Date(string='date of birth', related='patient_id.dateOfBirth')
    age = fields.Integer(string='Age', related='patient_id.age')
    appointment_status = fields.Selection(
        [('draft', 'draft'), ('confirmed', 'confirmed'), ('done', 'done'), ('cancelled', 'cancelled')], default='draft',
        string='Status')
    medicine_id = fields.One2many('hospital.medicine', 'appointment_id', string='medicines')

    # @api.model_create_multi
    # def create(self, vals):
    #     if self._context:
    #         for rec in vals:
    #             #rec['patient_id'] = self.env['res.partner'].search([('id', '=', self._context['patient_id'])])
    #             rec['patient_id'] = self._context['patient_id']
    #     return super(Appointment, self).create(vals)

    def confirm(self):
        self.appointment_status = 'confirmed'

    def done(self):
        self.appointment_status = 'done'

    def cancel(self):
        self.appointment_status = 'cancelled'


# class Prescription(models.Model):
#     _name = 'hospital.prescription'
#     _description = 'prescription information'
#     appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
#     medicine_id = fields.One2many('hospital.medicine', 'prescription_id', string='medicines')

class Medicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'medicine information'
    appointment_id = fields.Many2one('hospital.appointment', string='medicines')
    name = fields.Char(string='name')
    dosage = fields.Char(string='dosage')
    barcode = fields.Char(string='barcode')
    avgWeight = fields.Float(string='avg weight')