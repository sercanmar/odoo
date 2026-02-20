from odoo import models, fields, api

class Evento(models.Model):
    _name = 'gestion.evento'
    _description = 'Evento Comercial'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    
    fecha = fields.Date(string='Fecha', required=True)
    ubicacion = fields.Char(string='ubicacion', required=True)
    responsable_id = fields.Many2one('res.users', string='Responsable')
    asistentes_ids = fields.Many2many('gestion.asistente', string='Asistentes')
    sale_order_id = fields.Many2one('sale.order', string='Orden de Venta')
    purchase_order_id = fields.Many2one('purchase.order', string='Orden de Compra')

    _sql_constraints = [
        ('unique_nombre_fecha', 'unique(nombre, fecha)', 'No puede haber dos eventos con el mismo nombre y fecha.')
    ]

    total_asistentes = fields.Integer(string='Total Asistentes', compute='_compute_total_asistentes')

    @api.depends('asistentes_ids')
    def _compute_total_asistentes(self):
        for evento in self:
            evento.total_asistentes = len(evento.asistentes_ids)

    @api.onchange('nombre')
    def _aviso_multiplo_cinco(self):
        cantidad_actual = self.env['gestion.evento'].search_count([])
        if (cantidad_actual + 1) % 5 == 0:
            return {
                'warning': {
                    'title': 'aviso',
                    'message': 'con este evento llegarás a un múltiplo de 5 eventos.'
                }
            }
