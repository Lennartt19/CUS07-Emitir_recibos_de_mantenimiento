from flask import Blueprint, jsonify, request
from src.services.get.getTipoGastos import getTipoGastos

tipo_gastos = Blueprint('tipo_gastos', __name__)

@tipo_gastos.route('/getTipoGastosComunes')
def tipoGastosComunes():
    try:
        tipoGastos = getTipoGastos()
        if(len(tipoGastos) > 0):
            return jsonify({'tipoGastosComunes':tipoGastos, 'message':"SUCCESS", 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as error:
        return jsonify({'message':'ERROR', 'success':False})