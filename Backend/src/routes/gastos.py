from flask import Blueprint, jsonify, request
from src.services.get.getGastos import getGastos

gastos = Blueprint('gastos', __name__)

@gastos.route('/getPredios/<int:id>')
def Gastos(id):
    try:
        capturar_gastos = getGastos(id)
        if(len(capturar_gastos)>0):
            return jsonify({'gastos':capturar_gastos, 'message':"SUCCESS", 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as error:
        return jsonify({'message':'ERROR', 'success':False})