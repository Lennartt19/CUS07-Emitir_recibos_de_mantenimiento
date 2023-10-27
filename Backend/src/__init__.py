from flask import Flask
from config import DATABASE_CONNECTION_URI
from .routes.predio import predio
from .routes.predios import predios
from .routes.tabla_casas import tabla_casas
from .routes.descrip_gastos import descrip_gastos
from .routes.gastos_predio import gastos_predio
from .routes.registro_predio_estado import registro_predio_estado
from .routes.tipo_gastos import tipo_gastos
from .routes.gastos import gastos
from .routes.gasto_registrado import gasto_registrado

app = Flask(__name__)

def init_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.register_blueprint(descrip_gastos)
    app.register_blueprint(gasto_registrado)
    app.register_blueprint(gastos_predio)
    app.register_blueprint(gastos)
    app.register_blueprint(predio)
    app.register_blueprint(predios)
    app.register_blueprint(registro_predio_estado)
    app.register_blueprint(tabla_casas)
    app.register_blueprint(tipo_gastos)
    
    return app
