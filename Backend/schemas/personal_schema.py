from utils.ma import ma
from marshmallow import fields
from models.personal import Personal
from schemas.persona_schema import PersonaSchema
from schemas.rol_schema import RolSchema

class PersonalSchema(ma.SQLAlchemySchema):
    id_personal = fields.Integer()
    id_persona = fields.Integer()
    id_rol = fields.Integer()
    fecha_contrato = fields.Date()
    fecha_cese = fields.Date()

    persona = fields.Nested(PersonaSchema)
    rol = fields.Nested(RolSchema)
    class Meta:
        model = Personal
        fields = ('id_personal', 'id_persona', 'id_rol', 'fecha_contrato', 'fecha_cese')

personal_schema = PersonalSchema()
personales_schema = PersonalSchema(many=True)