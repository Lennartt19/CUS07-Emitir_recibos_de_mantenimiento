from flask import Blueprint, jsonify, request
from src.services.get.getPredios import getPredios

predios = Blueprint('predios', __name__)

@predios.route('/getPredios')
def Predios():
    try:
        capturar_predios = getPredios()
        if(len(capturar_predios) > 0):
            return jsonify({'predios':capturar_predios, 'message':"SUCCESS", 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as error:
        return jsonify({'message':'ERROR', 'success':False})