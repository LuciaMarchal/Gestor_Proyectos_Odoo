from datetime import timedelta
from odoo import models, fields, api

class Recordatorio(models.Model):
    _name = 'lmv_eventos.recordatorio'
    _description = 'Recordatorio de Evento'

    name = fields.Char('Nombre del Recordatorio', required=True)
    evento_id = fields.Many2one('lmv_eventos.evento', string='Evento', required=True, ondelete="cascade")
    fecha_envio = fields.Datetime('Fecha de envío del recordatorio', readonly=True)
    asistente_ids = fields.Many2many('lmv_eventos.asistente', string='Asistentes', compute='_compute_asistentes', store=True)
    
    @api.depends('evento_id')
    def _compute_asistentes(self):
        for recordatorio in self:
            # Muestra los asistentes del evento marcado
            if recordatorio.evento_id:
                recordatorio.asistente_ids = self.env['lmv_eventos.asistente'].search([('evento_ids', '=', recordatorio.evento_id.id)])
            else:
                recordatorio.asistente_ids = False