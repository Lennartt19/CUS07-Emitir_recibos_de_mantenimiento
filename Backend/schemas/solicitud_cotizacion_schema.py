from utils.ma import ma
from marshmallow import fields
from schemas.personal_schema import PersonalSchema
from schemas.estado_schema import EstadoSchema
from schemas.solicitud_schema import SolicitudSchema

class SolicitudCotizacionSchema(ma.Schema):
    id_solicitud = fields.Integer()
    id_personal = fields.Integer()
    fecha_cotizacion =fields.Date()
    importe = fields.Decimal()
    id_solicitud_cotizacion = fields.Integer()
    id_estado = fields.Integer()

    solicitud = fields.Nested(SolicitudSchema)
    personal = fields.Nested(PersonalSchema)
    estado = fields.Nested(EstadoSchema)