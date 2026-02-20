from odoo import models, fields

class Estudiante(models.Model):
    _name = 'academia.estudiante'
    _description = 'Estudiantes de la Academia'
    _rec_name = 'nombre'
    
    nombre = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email")
    curso_id = fields.Many2one('academia.curso', string="Curso")
    
    telefono = fields.Char(string='Telefono')
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")