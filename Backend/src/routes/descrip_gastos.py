from flask import Blueprint, jsonify, request
from src.services.get.getDescripGastos import getDescripGastos

descrip_gastos = Blueprint('descrip_gastos', __name__)

@descrip_gastos.route('/getTipoGastosComunes/<int:id>')
def descripGastos(id):
    try:
        tipoGastos = getDescripGastos(id)
        if(len(tipoGastos) > 0):
            return jsonify({'descripGastosComunes':tipoGastos, 'message':"SUCCESS", 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as error:
        return jsonify({'message':'ERROR', 'success':False})