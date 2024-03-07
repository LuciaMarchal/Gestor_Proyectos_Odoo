from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Evento(models.Model):
    _name = 'lmv_eventos.evento'
    _description = 'Evento'

    name = fields.Char('Nombre del Evento', required=True)
    fecha = fields.Datetime('Fecha del Evento', required=True)
    ubicacion = fields.Char('Ubicación del Evento', required=True)
    descripcion = fields.Text('Descripción del Evento', required=True)
    asistente_ids = fields.Many2many('lmv_eventos.asistente', string='Asistentes')
    recordatorio_ids = fields.One2many('lmv_eventos.recordatorio', 'evento_id', string='Recordatorios')
    informe_ids = fields.One2many('lmv_eventos.informe', 'evento_id', string='Informes')
    imagen = fields.Image(string="Imagen", store=True, help="Seleccionar imagen aquí")
    tipo = fields.Selection([
        ('1', 'Conferencia'),
        ('2', 'Charla'),
        ('3', 'Comida'),
        ('4', 'Cena'),
        ('5', 'Reunion'),
        ('6', 'Videollamada'),
        ('7', 'Fiesta')
    ], string='Tipo', required=True)
    
    @api.model
    def create(self, vals):
        evento = super(Evento, self).create(vals)
        # Crear el recordatorio correspondiente
        recordatorio_vals = {
            'name': 'Recordatorio para ' + evento.name,
            'evento_id': evento.id,
            'fecha_envio': fields.Datetime.to_string(fields.Datetime.from_string(evento.fecha) - timedelta(days=3))
        }
        self.env['lmv_eventos.recordatorio'].create(recordatorio_vals)
        return evento

    def write(self, vals):
        res = super(Evento, self).write(vals)
        if 'fecha' in vals:
            for evento in self:
                recordatorio = evento.recordatorio_ids
                if recordatorio:
                    recordatorio.fecha_envio = fields.Datetime.to_string(fields.Datetime.from_string(evento.fecha) - timedelta(days=3))
        return res
    
    @api.constrains("fecha")
    def _check_date(self):
        for record in self:
            if record.fecha < datetime.today():
                raise ValidationError("Introduce una fecha posterior a la actual")
            
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != descripcion)',
         "El nombre y la descripcion deben ser distintos"),
        ('name_unique','UNIQUE(name)',"El nombre tiene que ser unico"),
    ]
