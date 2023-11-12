from flask import Blueprint, render_template as rt, request, url_for, redirect,make_response
from flask import flash, request
from models.persona import Persona
from models.cuenta import Cuenta
from models.recaudacion import Recaudacion
from schemas.recaudacion_schema import recaudacion_schema,recaudaciones_schema
from models.mant_recibo import MantRecibo
from flask import jsonify
from models.predio import Predio
from models.cuenta_predio import CuentaPredio  
from utils.db import db
from models.casa import Casa
from models.recaudacion_estado import RecaudacionEstado
recaudacion = Blueprint('recaudaciones', __name__)

@recaudacion.route('/agregar', methods=['POST'])
def agregar_datos():
 
    id_cuenta = request.json.get('id_cuenta')
    id_mant_recibo = request.json.get('id_mant_recibo')    
    n_operacion = request.json.get('n_operacion')
    fecha_operacion = request.json.get('fecha_operacion')
    id_tipo_moneda = request.json.get('id_tipo_moneda')
    importe = request.json.get('importe')
    id_recaudacion_estado = request.json.get('id_recaudacion_estado')
    id_cuenta_predio = request.json.get('id_cuenta_predio')
    observacion = request.json.get('observacion')

    new_recaudacion = Recaudacion(id_cuenta,id_mant_recibo,n_operacion,fecha_operacion,id_tipo_moneda,importe,id_recaudacion_estado,id_cuenta_predio,observacion)
    db.session.add(new_recaudacion)
    db.session.commit()

    resultado = recaudacion_schema.dump(new_recaudacion)

    data={
        'message' : 'Nueva Recaudacion agregada',
        'status:' : 201,
        'data' : resultado
    }

    return make_response(jsonify(data),201)
    """
    num_recibo = request.form['num_recibo']
    # Obtener los datos enviados desde el formulario
    n_operacion = request.form['n_operacion']
    fecha_operacion = request.form['fecha_operacion']
    descripRecaud = request.form['id_recaudacion_estado']
    observacion= request.form['observacion']

    #cuenta = Cuenta.query.filter_by(ncuenta=num_cuenta).first()
    recibo = MantRecibo.query.filter_by(n_recibo=num_recibo).first()
    casa = Casa.query.filter_by(id_casa=recibo.id_casa).first()
    predio = Predio.query.filter_by(id_predio=casa.id_predio).first()
    persona = Persona.query.filter_by(id_persona=predio.id_persona).first()
    cuenta = Cuenta.query.filter_by(id_persona=persona.id_persona).first()
    cuentaPredio = CuentaPredio.query.filter_by(id_predio=predio.id_predio).first()
    recaudacionestado = RecaudacionEstado.query.filter_by(id_recaudacion_estado=descripRecaud).first()
    # Crear un nuevo o
    # bjeto en la base de datos con los datos proporcionados
    recaudacion = Recaudacion(
        id_cuenta=cuenta.id_cuenta,
        id_mant_recibo=recibo.id_mant_recibo ,
        n_operacion=n_operacion, 
        fecha_operacion=fecha_operacion,
        id_tipo_moneda=cuenta.id_tipo_moneda,
        importe=recibo.importe,
        id_recaudacion_estado=recaudacionestado.id_recaudacion_estado,
        id_cuenta_predio=cuentaPredio.id_cuenta_predio,
        observacion=observacion
    )
    db.session.add(recaudacion)
    db.session.commit()
    
    #Devolver una respuesta de éxito al cliente

    response = {
        'success': True,
        'message': 'Datos agregados correctamente'
    }
    return jsonify(response)
    """

@recaudacion.route('/BuscarRecaudacion', methods=['GET'])
def buscar_recaudaciones():
    recaudaciones = Recaudacion.query.all();
    resultado = recaudaciones_schema.dump(recaudaciones);
    response ={
        'success': True,
        'data': resultado
    }
    return make_response(jsonify(response),200)

@recaudacion.route('/editar/<int:id_recaudacion>', methods=['PUT'])
def editar_recaudacion(id_recaudacion):
    recaudacion = Recaudacion.query.get(id_recaudacion)

    if not recaudacion:
        data = {
            'message': 'Recaudacion no encontrada',
            'status': 404            
        }
        return make_response(jsonify(data),404)
    
    fecha_operacion = request.json.get('fecha_operacion')
    id_recaudacion_estado = request.json.get('id_recaudacion_estado')
    observacion = request.json.get('observacion')

    recaudacion.fecha_operacion = fecha_operacion
    recaudacion.id_recaudacion_estado = id_recaudacion_estado
    recaudacion.observacion = observacion

    db.session.commit()
    resultado = recaudacion_schema.dump(recaudacion)

    data = {
        'message': 'Recaudacion actualizada',
        'status': 200,
        'data': resultado
    }
    
    return make_response(jsonify(data),200)

    """
    if request.method == 'POST':
        # Obtener los datos actualizados del formulario
        # y actualizar la recaudación en la base de datos
        
        recaudacion.fecha_operacion = request.form['fecha-operacion-input']       
        recaudacion.id_recaudacion_estado = request.form['EstadoR-input']        
        recaudacion.observacion = request.form['observacion-input']

        # Guardar los cambios en la base de datos
        db.session.commit()

        # Redirigir a la página principal de recaudaciones
        return redirect(url_for('recaudaciones.recaudaciones'))

    # Renderizar la plantilla de edición con los datos de la recaudación
    return rt("editar_recaudacion.html", recaudacion=recaudacion)
    """

@recaudacion.route('/eliminar/<int:id_recaudacion>', methods=['DELETE'])
def eliminar_recaudacion(id_recaudacion):
    recaudacion = Recaudacion.query.get(id_recaudacion)

    if not recaudacion:
        data = {
            'message': 'Recaudacion no encontrada',
            'status': 404            
        }
        return make_response(jsonify(data),404)   

    db.session.delete(recaudacion)
    db.session.commit()

    data = {
        'message': 'Recaudacion eliminada',
        'status': 200        
    } 

    return make_response(jsonify(data),200)

    """
    if request.method == 'POST':
        # Eliminar la recaudación de la base de datos
        db.session.delete(recaudacion)
        db.session.commit()

        # Redirigir a la página principal de recaudaciones
        return redirect(url_for('recaudaciones.recaudaciones'))

    # Renderizar la plantilla de confirmación de eliminación
    return rt("eliminar_recaudacion.html", recaudacion=recaudacion)
        """