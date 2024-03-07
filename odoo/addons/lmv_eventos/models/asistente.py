from odoo import models, fields, api
from odoo.addons import lmv_eventos

class Asistente(models.Model):
    _name = 'lmv_eventos.asistente'
    _description = 'Asistentes al Evento'

    name = fields.Char('Nombre', required=True)
    email = fields.Char('Correo Electrónico', required=True)
    evento_ids = fields.Many2many('lmv_eventos.evento', string='Eventos')
    imagen = fields.Image(string="Imagen", store=True, help="Seleccionar imagen aquí")

    @api.model_create_single
    def create(self, vals):
        # Creamos el asistente
        asistente = super(Asistente, self).create(vals)

        # Creamos el usuario asociado al asistente
        user_vals = {
            'name': asistente.name,
            'login': asistente.email,
            'password': 'contrasena',  # Asigna aquí la contraseña deseada
            'groups_id': [(6, 0, [
                self.env.ref('lmv_eventos.lmv_eventos_asistente_group').id,
                self.env.ref('base.group_user').id
            ])]
        }
        self.env['res.users'].create(user_vals)

        return asistente