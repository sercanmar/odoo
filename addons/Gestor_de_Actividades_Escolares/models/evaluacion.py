from odoo import models,fields

class Evaluacion(models.Model):
    _name = 'academia.evaluacion'
    _description = 'Evaluaciones estudiantes'
    _rec_name = 'nombre'
    
    nota = fields.Float(string="Calificación")
    comentario = fields.Text(string="Comentar/Observaciones")
    
    estudiante_id =fields.Many2one(
        'academia.estudiante',
        string="Estudiante"
        
    )
    curso_id = fields.Many2one(
        'academia.curso',
        string="Curso"
    )