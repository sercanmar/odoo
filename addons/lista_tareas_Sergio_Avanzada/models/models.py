import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ListaTareas(models.Model):

    _name = 'lista_tareas.lista'
    _description = 'Lista de Tareas Avanzada'

    tarea = fields.Char(string="Tarea", required=True)
    etiqueta_id = fields.Many2one('lista_tareas.etiqueta', string="Etiqueta")
    tiempo_estimado = fields.Float(string="Tiempo Estimado (horas)")

    urgente = fields.Boolean(compute="_compute_urgente", store=True)

    @api.depends('tiempo_estimado')
    def _compute_urgente(self):
        for record in self:
            record.urgente = record.tiempo_estimado > 5


class Etiqueta(models.Model):
    _name = 'lista_tareas.etiqueta'
    _description = 'Etiqueta de Tareas'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    tarea_ids = fields.One2many('lista_tareas.lista', 'etiqueta_id', string="Tareas")

    _sql_constraints = [
        ('nombre_uniq', 'unique(nombre)', 'El nombre de la etiqueta debe ser único.')
    ]

    def verificar_tiempo_acumulado(self):
        etiquetas = self.search([])
        for etiqueta in etiquetas:
            total_tiempo = sum(etiqueta.tarea_ids.mapped('tiempo_estimado'))
            if total_tiempo > 20:
                _logger.info(f"La etiqueta '{etiqueta.nombre}' tiene más de 20 horas acumuladas.")
                self.env['mail.message'].create({
                    'body': f"La etiqueta '{etiqueta.nombre}' tiene más de 20 horas acumuladas.",
                    'subject': "Alerta de tiempo acumulado",
                    'model': self._name,
                    'res_id': etiqueta.id,
                })