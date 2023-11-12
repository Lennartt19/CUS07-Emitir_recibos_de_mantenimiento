from flask import Blueprint, render_template as rt
from models.solicitud import Solicitud
from models.solicitud_cotizacion import SolicitudCotizacion
from schemas.solicitud_schema import SolicitudSchema
from schemas.solicitud_cotizacion_schema import SolicitudCotizacionSchema

solicitud_cotizacion = Blueprint('solicitud_cotizacion', __name__, url_prefix="/solicitud") #al llamar el blue print en base sería (NomreBP.FuncionAsociadaARuta)

@solicitud_cotizacion.route('/<id_solicitud>', methods=['GET'])
def cotizar(id_solicitud):
    
    solicitud_cotizacion = SolicitudCotizacion.query.filter_by(id_solicitud=id_solicitud).first()
    
    if solicitud_cotizacion:
        cotizacion_realizada = "Realizada"
        data = SolicitudCotizacionSchema().dump(solicitud_cotizacion)
    else:
        cotizacion_realizada = "No realizada"
        solicitud=Solicitud.query.get(id_solicitud)
        data = SolicitudSchema().dump(solicitud)
    
    return rt("SeguirSolicitudCotizacion/cotizacion.html",data=data,cotizacion_realizada=cotizacion_realizada)