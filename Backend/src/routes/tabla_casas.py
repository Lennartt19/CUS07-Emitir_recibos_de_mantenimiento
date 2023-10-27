from flask import Blueprint, jsonify, request
from src.services.get.getTablaCasas import getTablaCasas

tabla_casas = Blueprint('tabla_casas', __name__)

@tabla_casas.route('/getPredios/<int:id>/getCasas')
def casas(id):
    try:
        casas = getTablaCasas(id)
        if(len(casas)>0):
            return jsonify({'casas':casas, 'message':"SUCCESS", 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as error:
        return jsonify({'message':'ERROR', 'success':False})