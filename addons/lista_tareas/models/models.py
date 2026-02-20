from odoo import models, fields

class ListaTareas(models.Model):
    _name = 'lista.tareas'
    _description = 'Modelo para gestionar tareas'

    name = fields.Char(string="Título de la Tarea", required=True)
    descripcion = fields.Text(string="Descripción")
    realizada = fields.Boolean(string="¿Completada?", default=False)
