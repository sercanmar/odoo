from odoo import models, fields, api

class Asistente(models.Model):
    _name = 'gestion.asistente'
    _description = 'Asistente'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email', required=True)
    eventos_ids = fields.Many2many('gestion.evento', string='Eventos')
