from flask import Blueprint, render_template as rt, flash, redirect, url_for, request, jsonify
from models.banco import Banco
from models.casa import Casa
from models.cuenta import Cuenta
from models.casa_estado import CasaEstado
from models.cuenta_predio import CuentaPredio
from models.estado import Estado
from models.recaudacion_estado import RecaudacionEstado
from models.mant_recibo import MantRecibo
from models.recibo_estado import ReciboEstado
from models.persona import Persona
from models.predio import Predio
from models.recaudacion import Recaudacion
from models.tipo_autorizacion import TipoAutorizacion
from models.tipo_documento import TipoDocumento
from models.tipo_moneda import TipoMoneda
from models.tipo_predio import TipoPredio
from models.ubigeo import Ubigeo

from utils.db import db
from utils.json import model_to_dict

vista = Blueprint('vista', __name__, url_prefix="/vista")

@vista.route('/')
def vista_principal(): #esta función debe coincidir con el url_for del html (base)
    banco =Banco.query.all()
    casa =Casa.query.all()
    casaEstado=CasaEstado.all()
    cuenta = Cuenta.query.all()
    cuentaPredio=CuentaPredio.query.all()
    estado =Estado.query.all()
    recaudacionEstado =RecaudacionEstado.query.all()
    mantRecibo =MantRecibo.query.all()
    persona =Persona.query.all()
    predio =Predio.query.all()
    recaudacion =Recaudacion.query.all()
    reciboEstado =ReciboEstado.query.all()
    tipoAutorizacion =TipoAutorizacion.query.all()
    tipoDocumento =TipoDocumento.query.all()
    tipoMoneda =TipoMoneda.query.all()
    tipoPredio =TipoPredio.query.all()
    ubigeo =Ubigeo.query.all()

    data_banco = []
    data_casa = []
    data_casaEstado = []
    data_cuenta = []
    data_cuentaPredio = []
    data_estado = []
    data_recaudacionEstado = []
    data_mantRecibo = []
    data_persona = []
    data_predio =[]
    data_recaudacion = []
    data_reciboEstado = []
    data_tipoAutorizacion = []
    data_tipoDocumento = []
    data_tipoMoneda =[]
    data_tipoPredio = []
    data_ubigeo = []
    
    # Crear una lista para almacenar los datos convertidos a json
    for obj in banco:
        x = model_to_dict(obj)
        data_banco.append(x)
    for obj in casa:
        x = model_to_dict(obj)
        data_casa.append(x)
    for obj in casaEstado:
        x = model_to_dict(obj)
        data_casaEstado.append(x)
    for obj in cuenta:
        x = model_to_dict(obj)
        data_cuenta.append(x)
    for obj in cuentaPredio:
        x = model_to_dict(obj)
        data_cuentaPredio.append(x)
    for obj in estado:
        x = model_to_dict(obj)
        data_estado.append(x)
    for obj in recaudacionEstado:
        x = model_to_dict(obj)
        data_recaudacionEstado.append(x)
    for obj in mantRecibo:
        x = model_to_dict(obj)
        data_mantRecibo.append(x)
    for obj in persona:
        x = model_to_dict(obj)
        data_persona.append(x)
    for obj in predio:
        x = model_to_dict(obj)
        data_predio.append(x)
    for obj in recaudacion:
        x = model_to_dict(obj)
        data_recaudacion.append(x)
    for obj in reciboEstado:
        x = model_to_dict(obj)
        data_reciboEstado.append(x)
    for obj in tipoAutorizacion:
        x = model_to_dict(obj)
        data_tipoAutorizacion.append(x)
    for obj in tipoDocumento:
        x = model_to_dict(obj)
        data_tipoDocumento.append(x)
    for obj in tipoMoneda:
        x = model_to_dict(obj)
        data_tipoMoneda.append(x)
    for obj in tipoPredio:
        x = model_to_dict(obj)
        data_tipoPredio.append(x)
    for obj in ubigeo:
        x=model_to_dict(obj)
        data_ubigeo.append(x)
    
    result = {
        'banco': data_banco,
        'casa': data_casa,
        'casaEstado': data_casaEstado,
        'cuenta': data_cuenta,
        'cuentaPredio': data_cuentaPredio,
        'estado': data_estado,
        'estadoRecaudacion': data_recaudacionEstado,
        'mantRecibo': data_mantRecibo,
        'persona':data_persona,
        'predio':data_predio,
        'recaudacion':data_recaudacion,
        'reciboEstado':data_reciboEstado,
        'tipoAutorizacion': data_tipoAutorizacion,
        'tipoDocumento': data_tipoDocumento,
        'tipoMoneda':data_tipoMoneda,
        'tipoPredio': data_tipoPredio,
        'ubigeo': data_ubigeo
    }

    return jsonify(result)

@vista.route('/recaudacion')
def vista_recaudacion():
    query =Recaudacion.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'recaudacion': data
    }
    return jsonify(result)

@vista.route('/recaudacion_estado')
def vista_recaudacion_estado():
    query =RecaudacionEstado.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'recaudacion_estado': data
    }
    return jsonify(result)

@vista.route('/persona')
def vista_persona():
    query =Persona.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'persona': data
    }
    return jsonify(result)

@vista.route('/predio')
def vista_predio():
    query =Predio.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'predio': data
    }
    return jsonify(result)

@vista.route('/tipo_documento')
def vista_tipo_documento():
    query =TipoDocumento.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'tipo_documento': data
    }
    return jsonify(result)

@vista.route('/banco')
def vista_banco():
    query =Banco.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'banco': data
    }
    return jsonify(result)

@vista.route('/cuenta')
def vista_cuenta():
    query =Cuenta.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'cuenta': data
    }
    return jsonify(result)

@vista.route('/tipo_moneda')
def vista_tipo_moneda():
    query =TipoMoneda.query.all()
    data = []
    for obj in query:
        data.append(model_to_dict(obj))
    result = {
        'tipo_moneda': data
    }
    return jsonify(result)
