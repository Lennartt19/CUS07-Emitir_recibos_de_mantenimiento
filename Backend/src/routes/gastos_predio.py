from flask import Blueprint, jsonify, request
from src.services.get.getGastosPredio import getGastosPredio
from src.services.post.postGastosPredio import postGastosPredio
from src.services.put.putGastosPredio import putGastosPredio

gastos_predio = Blueprint('gastos_predio', __name__)

@gastos_predio.route('/getGastosPredios/<int:id>')
def gastosPredios(id):
    try:
        gastosPredios = getGastosPredio(id)
        if(len(gastosPredios) > 0):
            return jsonify({'gastoPredioDetalle':gastosPredios, 'message':"SUCCESS", 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as error:
        return jsonify({'message':'ERROR', 'success':False})

@gastos_predio.route('/insertarGastoPredio', methods = ['POST'])
def insertar_gasto_predio():
    try:
        data = request.get_json()
        id_predio_gastos = data['id_predio_gastos']
        id_gasto = data['id_gasto']
        importe = data['importe']
        if(postGastosPredio(id_predio_gastos, id_gasto, importe)):
            return jsonify({'message': data, 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as error:
        return jsonify({'message':'ERROR', 'success':False})

@gastos_predio.route('/actualizarGastoPredio', methods = ['PUT'])
def actualizar_gasto_predio():
    try:
        data = request.get_json()
        id_predio_gastos_det = data['id_predio_gastos_det']
        importe = data['importe']
        if(putGastosPredio(id_predio_gastos_det, importe)):
            return jsonify({'message': data, 'success':True})
        else:
            return jsonify({'message':"NOT FOUND", 'success':True})
    except Exception as error:
        return jsonify({'message':'ERROR', 'success':False})
    