from odoo import models, fields, api

class lista_tareas(models.Model):
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'
    _rec_name = "tarea"

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()

    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            if record.prioridad > 30:
                record.urgente = True
            else:
                record.urgente = False