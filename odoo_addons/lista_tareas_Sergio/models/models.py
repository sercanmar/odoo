from odoo import models, fields
from datetime import datetime, timedelta

class ListaTareas(models.Model):
    _name = 'lista.tareas'
    _description = 'Modelo para gestionar tareas'

    name = fields.Char(string="Título de la Tarea", required=True)
    descripcion = fields.Text(string="Descripción")
    realizada = fields.Boolean(string="¿Completada?", default=False)

    fecha_limite = fields.Date(
        string='Fecha Limite',
        default=lambda self: (datetime.now() + timedelta(days=7)).date(),
        help='Fecha limite para completar la tarea'
    )

    def verificar_tareas_atrasadas(self):
        for tarea in self:
            if tarea.fecha_limite and tarea.fecha_limite < fields.Date.today():
                print(f"La tarea {tarea.name} está atrasada.")
