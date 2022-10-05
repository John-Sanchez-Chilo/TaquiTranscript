from email import contentmanager
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from backend.models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()

################# Cliente ################################

@task_blueprint.route('/cliente/add_cliente', methods=['POST'])
@cross_origin()
def create_cliente():
    content = model.add_cliente(request.json['nombre'], request.json['correo'], request.json['contrasena'])
    return jsonify(content)

@task_blueprint.route('/cliente/get_cliente', methods=['POST'])
@cross_origin()
def get_cliente():
    return jsonify(model.get_cliente(int(request.json['ID_cliente'])))

@task_blueprint.route('/cliente/get_clientes', methods=['POST'])
@cross_origin()
def get_clientes():
    return jsonify(model.get_clientes())

@task_blueprint.route('/cliente/delete_cliente', methods=['POST'])
@cross_origin()
def delete_cliente():
    return jsonify(model.delete_cliente(int(request.json['ID_cliente'])))


################# Caso ################################

@task_blueprint.route('/caso/add_caso', methods=['POST'])
@cross_origin()
def create_caso():
    content = model.add_caso(request.json['titulo'], request.json['fecha_inicio'], request.json['estado'], request.json['descripcion'])
    return jsonify(content)

@task_blueprint.route('/caso/get_caso', methods=['POST'])
@cross_origin()
def get_caso():
    return jsonify(model.get_caso(int(request.json['ID_caso'])))

@task_blueprint.route('/caso/get_casos', methods=['POST'])
@cross_origin()
def get_casos():
    return jsonify(model.get_casos())

@task_blueprint.route('/caso/delete_caso', methods=['POST'])
@cross_origin()
def delete_caso():
    return jsonify(model.delete_caso(int(request.json['ID_caso'])))