from odoo import models, fields, api

class Informe(models.Model):
    _name = 'lmv_eventos.informe'
    _description = 'Informe de Asistencia'

    name = fields.Char('Nombre del Informe', required=True)
    fecha_generacion = fields.Datetime('Fecha de Generación', default=fields.datetime.now(), readonly=True)
    evento_id = fields.Many2one('lmv_eventos.evento', string='Evento', required=True, ondelete="cascade")
    asistente_ids = fields.Many2many('lmv_eventos.asistente', string='Asistentes', compute='_compute_asistentes', store=True)
    asistentes_totales = fields.Integer('Asistentes totales', compute="_asistentes_totales", store=True)

    @api.depends('evento_id')
    def _compute_asistentes(self):
        for informe in self:
            if informe.evento_id:
                informe.asistente_ids = self.env['lmv_eventos.asistente'].search([('evento_ids', '=', informe.evento_id.id)])
            else:
                informe.asistente_ids = False

    @api.depends('asistente_ids')
    def _asistentes_totales(self):
        for informe in self:
            informe.asistentes_totales = len(informe.asistente_ids)
