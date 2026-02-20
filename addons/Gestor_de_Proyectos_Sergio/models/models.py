from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Proyecto(models.Model):
    _name = 'gestor.proyecto'
    _description = 'Gestor de Proyectos'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre del Proyecto', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True, default=fields.Date.today)
    fecha_fin = fields.Date(string='Fecha de Fin')
    responsable_ids = fields.Many2many('res.users', string='Responsables')
    tarea_ids = fields.One2many('gestor.tarea', 'proyecto_id', string='Tareas')
    total_tareas = fields.Integer(string='Total de Tareas', compute='_compute_total_tareas')
    _sql_constraints = [
        ('nombre_unico', 'unique(nombre)', 'El nombre del proyecto debe ser único.')
    ]

    @api.depends('tarea_ids')
    def _compute_total_tareas(self):
        for proyecto in self:
            proyecto.total_tareas = len(proyecto.tarea_ids)

class Tarea(models.Model):
    _name = 'gestor.tarea'
    _description = 'Tarea'

    nombre = fields.Char(string='Nombre de la Tarea', required=True)
    descripcion = fields.Text(string='Descripción')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada')
    ], string='Estado', default='pendiente')
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True, default=fields.Date.today)
    fecha_limite = fields.Date(string='Fecha Límite', required=True)
    responsable_id = fields.Many2one('res.users', string='Responsable')
    proyecto_id = fields.Many2one('gestor.proyecto', string='Proyecto Relacionado')

    @api.constrains('fecha_inicio', 'fecha_limite')
    def _check_fecha_limite(self):
        for tarea in self:
            if tarea.fecha_inicio and tarea.fecha_limite and tarea.fecha_inicio > tarea.fecha_limite:
                raise ValidationError('La fecha de inicio no puede ser posterior a la fecha límite.')

class Responsable(models.Model):
    _inherit = 'res.users'
    proyectos_ids = fields.Many2many('gestor.proyecto', string='Proyectos Asignados')
    tareas_ids = fields.One2many('gestor.tarea', 'responsable_id', string='Tareas Asignadas')
