from odoo import models, fields
class Curso(models.Model):
    _name = 'academia.curso'
    _description = 'Cursos de la Academia'
    nombre = fields.Char(string="Nombre del Curso", required=True)
    descripcion = fields.Text(string="Descripción")
    profesor_id = fields.Many2one('res.users', string="Profesor")
    estudiantes_ids = fields.One2many('academia.estudiante', 'curso_id',
    string="Estudiantes")

