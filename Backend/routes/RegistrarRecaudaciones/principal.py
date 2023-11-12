from flask import Blueprint, render_template as rt, request, url_for, redirect
from models.recaudacion import Recaudacion
from schemas.recaudacion_schema import RecaudacionSchema
from models.mant_recibo import MantRecibo
from schemas.mant_recibo_schema import MantReciboSchema


principal = Blueprint('principal', __name__)

@principal.route('/principal', methods=['POST','GET'])
def recaudaciones():
    #Obtener todas las recaudaciones
    recaudaciones= Recaudacion.query.all()
    recibos = MantRecibo.query.all()
    # Serializar los objetos por medio de schemas
    recaudaciones_serializadas=RecaudacionSchema(many=True).dump(recaudaciones)
    recibos_serializados=MantReciboSchema(many=True).dump(recibos)
    
    return rt("RegistrarRecaudaciones/recaudacion.html",recaudaciones=recaudaciones_serializadas, 
        recibos=recibos_serializados)