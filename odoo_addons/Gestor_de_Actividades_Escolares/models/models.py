from odoo import models, fields
class Curso(models.Model):
    _name = 'academia.curso'
    _description = 'Cursos de la Academia'
    nombre = fields.Char(string="Nombre del Curso", required=True)
    descripcion = fields.Text(string="Descripción")
    profesor_id = fields.Many2one('res.users', string="Profesor")
    estudiantes_ids = fields.One2many('academia.estudiante', 'curso_id', string="Estudiantes")

    #notificación mostrada arriba a la derecha
    
@api.onchange('etiqueta_id')
def _onchange_etiqueta_id(self):
    if self.etiqueta_id:
        tarea_count = self.env['lista_tareas_avanzada.lista'].search_count(
            [('etiqueta_id', '=', self.etiqueta_id.id)])
        if tarea_count > 10:
            _logger.info(f"____NOTIFICACIÓN___________La etiqueta '{self.etiqueta_id.nombre}' tiene más de 10 tareas.")
            return {
                'warning': {
                    'title': "Notificación",
                    'message': f"La etiqueta '{self.etiqueta_id.nombre}' tiene más de 10 tareas.",
                    'type': 'notification'
                } }

    
            

class Estudiante(models.Model):
    _name = 'academia.estudiante'
    _description = 'Estudiantes de la Academia'
    nombre = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email")
    curso_id = fields.Many2one('academia.curso', string="Curso")

class Evaluacion(models.Model):
    _name = 'academia.evaluacion'
    _description = 'Evaluación del Estudiante'
    _rec_name = 'name' # Usaremos el nombre del examen como identificador

    name = fields.Char(string='Título de la Evaluación', required=True)
    calificacion = fields.Float(string='Nota')
    fecha = fields.Date(string='Fecha', default=fields.Date.today)
    

    # Relaciones obligatorias: Una nota pertenece a un Estudiante y a un Curso
    estudiante_id = fields.Many2one('academia.estudiante', string='Estudiante', required=True)
    curso_id = fields.Many2one('academia.curso', string='Curso', required=True)
