from email import contentmanager
from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones
from werkzeug import secure_filename
import os
from models.task_model import TaskModel

task_blueprint = Blueprint('task_blueprint', __name__)

model = TaskModel()

################# Cliente ################################
@task_blueprint.route('/cliente/login_cliente', methods=['POST'])
@cross_origin()
def login_cliente():
    content = model.login_cliente(request.json['correo'], request.json['contrasena'])
    return jsonify(content)


@task_blueprint.route('/cliente/add_cliente', methods=['POST'])
@cross_origin()
def create_cliente():
    content = model.add_cliente(request.json['correo'], request.json['contrasena'],request.json['nombre'],request.json['ape_paterno'],request.json['ape_materno'])
    #me parece que no deberia retonar nada, solo seria GET
    return jsonify(content)

@task_blueprint.route('/cliente/get_cliente', methods=['POST'])
@cross_origin()
def get_cliente():
    return jsonify(model.get_cliente(int(request.json['id_cliente'])))

@task_blueprint.route('/cliente/get_clientes', methods=['POST'])
@cross_origin()
def get_clientes():
    return jsonify(model.get_clientes())

@task_blueprint.route('/cliente/delete_cliente', methods=['POST'])
@cross_origin()
def delete_cliente():
    return jsonify(model.delete_cliente(int(request.json['id_cliente'])))


################# Caso ################################

@task_blueprint.route('/caso/add_caso', methods=['POST'])
@cross_origin()
def create_caso():
    content = model.add_caso(request.json['titulo'], request.json['descripcion'], request.json['id_cliente'])
    return jsonify(content)

@task_blueprint.route('/caso/get_caso', methods=['POST'])
@cross_origin()
def get_caso():
    return jsonify(model.get_caso(int(request.json['id_caso'])))

@task_blueprint.route('/caso/get_casos', methods=['POST'])
@cross_origin()
def get_casos():
    return jsonify(model.get_casos())

@task_blueprint.route('/caso/get_casos_cliente', methods=['POST'])
@cross_origin()
def get_casos_cliente():
    return jsonify(model.get_casos_cliente(int(request.json['id_cliente'])))

@task_blueprint.route('/caso/delete_caso', methods=['POST'])
@cross_origin()
def delete_caso():
    return jsonify(model.delete_caso(int(request.json['id_caso'])))


################# Sesion ################################

@task_blueprint.route('/sesion/add_sesion', methods=['POST'])
@cross_origin()
def create_sesion():
    content = model.add_sesion(request.json['fecha'], request.json['descripcion'], request.json['id_caso'])
    return jsonify(content)

@task_blueprint.route('/sesion/get_sesion', methods=['POST'])
@cross_origin()
def get_sesion():
    return jsonify(model.get_sesion(int(request.json['id_sesion'])))

@task_blueprint.route('/sesion/get_sesiones', methods=['POST'])
@cross_origin()
def get_sesiones():
    return jsonify(model.get_sesiones())

@task_blueprint.route('/sesion/get_sesiones_caso', methods=['POST'])
@cross_origin()
def get_sesiones_caso():
    return jsonify(model.get_sesiones_caso(int(request.json['id_caso'])))

@task_blueprint.route('/sesion/delete_sesion', methods=['POST'])
@cross_origin()
def delete_sesion():
    return jsonify(model.delete_sesion(int(request.json['id_sesion'])))



################# participante ################################

@task_blueprint.route('/participante/add_participante', methods=['POST'])
@cross_origin()
def create_participante():
    content = model.add_participante(request.json['nombre'], request.json['ape_paterno'], request.json['ape_materno'], request.json['tipo'], request.json['id_sesion'])
    return jsonify(content)

@task_blueprint.route('/participante/get_participante', methods=['POST'])
@cross_origin()
def get_participante():
    return jsonify(model.get_participante(int(request.json['id_participante'])))

@task_blueprint.route('/participante/get_participantes', methods=['POST'])
@cross_origin()
def get_participantes():
    return jsonify(model.get_participantes())

@task_blueprint.route('/participante/get_participantes_sesion', methods=['POST'])
@cross_origin()
def get_participantes_sesion():
    return jsonify(model.get_participantes_sesion(int(request.json['id_sesion'])))

@task_blueprint.route('/participante/delete_participante', methods=['POST'])
@cross_origin()
def delete_participante():
    return jsonify(model.delete_participante(int(request.json['id_participante'])))


################# Declaracion ################################

def allowed_file(file):
    ALLOWED_EXTENSIONS=set(['mp3','mp4','wav','flac'])
    file = file.split('.')
    if type[1] in ALLOWED_EXTENSIONS:
        return True
    return False

def convertir(file):
    return "Esta es la transcripcion"

@task_blueprint.route('/declaracion/add_declaracion', methods=['POST'])
@cross_origin()
def create_declaracion():
    file=request.files["uploadFile"]
    filename=secure_filename(file.filename)
    transcript=""
    if(allowed_file(filename)):
        transcript=convertir(file)
        #file.save(os.path.join("static/uploads",filename))
    content = model.add_declaracion(request.json['titulo'], request.json['tipo'], transcript, request.json['id_participante'])
    return jsonify(content)

@task_blueprint.route('/declaracion/get_declaracion', methods=['POST'])
@cross_origin()
def get_declaracion():
    return jsonify(model.get_declaracion(int(request.json['id_declaracion'])))

@task_blueprint.route('/declaracion/get_declaraciones', methods=['POST'])
@cross_origin()
def get_declaraciones():
    return jsonify(model.get_declaraciones())

@task_blueprint.route('/declaracion/get_declaraciones_participante', methods=['POST'])
@cross_origin()
def get_declaraciones_participante():
    return jsonify(model.get_declaraciones_participante(int(request.json['id_participante'])))

@task_blueprint.route('/declaracion/delete_declaracion', methods=['POST'])
@cross_origin()
def delete_declaracion():
    return jsonify(model.delete_declaracion(int(request.json['id_declaracion'])))
