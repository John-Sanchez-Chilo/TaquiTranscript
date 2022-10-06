from models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()


################### CLiente ################################

    # Funcion para login
    def login_cliente(self,correo,contrasena):
        params = {
            'correo' : correo,
            'contrasena' : contrasena,
        }
        rv = self.mysql_pool.execute("SELECT id_cliente, correo, contrasena from cliente where correo=%(correo)s", params)
        data = []
        if(len(rv)>0):
            content = {}
            for result in rv:
                content = {'id_cliente': result[0], 'correo': result[1], 'contrasena': result[2]}
                data.append(content)
                content = {}
            return data
        else:
            return data


    # Funcion para agregar un cliente
    def add_cliente(self, correo, contrasena,nombre, ape_paterno, ape_materno):
        params = {
            
            'correo' : correo,
            'contrasena' : contrasena,
            'nombre' : nombre,
            'ape_paterno' : ape_paterno,
            'ape_materno' : ape_materno,
        }  
        query = """insert into cliente ( correo, contrasena,nombre,ape_paterno,ape_materno)
            values ( %(correo)s, %(contrasena)s,%(nombre)s,%(ape_paterno)s,%(ape_materno)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id_cliente': cursor.lastrowid, 'nombre': nombre, 'correo': correo, 'contrasena': contrasena}
        return data

    # Funcion para obtener un cliente por su ID
    def get_cliente(self, id_cliente):
        params = {'id_cliente' : id_cliente}      
        rv = self.mysql_pool.execute("SELECT id_cliente, nombre, ape_paterno, ape_materno, correo from cliente where id_cliente=%(id_cliente)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_cliente': result[0], 'nombre': result[1], 'ape_paterno': result[2], 'correo': result[4]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para obtener todos los clientes
    def get_clientes(self):
        rv = self.mysql_pool.execute("SELECT * from cliente")  
        data = []
        content = {}
        for result in rv:
            content = {'id_cliente': result[0], 'nombre': result[1], 'ape_paterno': result[2], 'correo': result[4]}
            data.append(content)
            content = {}
        return data

    # Funcion para eliminar un cliente
    def delete_cliente(self, id_cliente):
        params = {'id_cliente' : id_cliente}      
        query = """delete from cliente where id_cliente = %(id_cliente)s"""    
        self.mysql_pool.execute(query, params, commit=True)   
        #me parece que no deberia retornar y ser DELETE
        data = {'result': 1}
        return data


################### Caso ################################

    # Funcion para agregar un caso
    def add_caso(self, titulo, descripcion, id_cliente):
        params = {
            'titulo' : titulo,
            'descripcion' : descripcion,
            'id_cliente' : id_cliente
        }  
        query = """insert into caso (titulo, descripcion, fecha_inicio, estado, id_cliente)
            values (%(titulo)s, curdate(), Activo, %(descripcion)s,%(id_cliente)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id': cursor.lastrowid_cliente, 'titulo': titulo, 'descripcion': descripcion, 'fecha_inicio': cursor.fecha_inicio, 'fecha_fin': cursor.lastrowfecha_fin,'estado': cursor.estado }
        return data

    # Funcion para obtener un caso por su ID
    def get_caso(self, id_caso):
        params = {'id_caso' : id_caso}      
        rv = self.mysql_pool.execute("SELECT * from caso where id_caso=%(id_caso)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_caso': result[0], 'titulo': result[1], 'descripcion': result[2], 'fecha_inicio': result[3], 'fecha_fin': result[4], 'estado': result[5]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los casos
    def get_casos(self):
        rv = self.mysql_pool.execute("SELECT * from caso")  
        data = []
        content = {}
        for result in rv:
            content = {'id_caso': result[0], 'titulo': result[1], 'descripcion': result[2], 'fecha_inicio': result[3], 'fecha_fin': result[4], 'estado': result[5]}
            data.append(content)
            content = {}
        return data
    
    #Funcion para obtener todos los casos de un cliente especifico
    def get_casos_cliente(self,id_cliente):
        params = {'id_cliente' : id_cliente} 
        rv = self.mysql_pool.execute("SELECT * from caso where id_cliente=%(id_cliente)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_caso': result[0], 'titulo': result[1], 'descripcion': result[2], 'fecha_inicio': result[3], 'fecha_fin': result[4], 'estado': result[5]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para eliminar un caso
    def delete_caso(self, id_caso):
        params = {'id_caso' : id_caso}      
        query = """delete from caso where id_caso = %(id_caso)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
        


################### Sesion ################################

    # Funcion para agregar una sesion
    def add_sesion(self,fecha, descripcion, id_caso):
        params = {
            'fecha' : fecha,
            'descripcion' : descripcion,
            'id_caso': id_caso
        }  
        query = """insert into sesion (fecha, descripcion, id_caso )
            values (%(fecha)s, %(descripcion)s, %(id_caso)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id': cursor.lastrowid, 'fecha': fecha, 'descripcion': descripcion, 'id_caso': id_caso}
        return data

    # Funcion para obtener un sesion por su ID
    def get_sesion(self, id_sesion):
        params = {'id_sesion' : id_sesion}      
        rv = self.mysql_pool.execute("SELECT * from sesion where id_sesion=%(id_sesion)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_sesion': result[0], 'fecha': result[1], 'descripcion': result[2]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los sesiones
    def get_sesiones(self):
        rv = self.mysql_pool.execute("SELECT * from sesion")  
        data = []
        content = {}
        for result in rv:
            content = {'id_sesion': result[0], 'fecha': result[1], 'descripcion': result[2], 'id_caso': result[3]}
            data.append(content)
            content = {}
        return data
    
    #Funcion para obtener todos los sesiones de un caso especifico
    def get_sesiones_caso(self,id_caso):
        params = {'id_caso' : id_caso} 
        rv = self.mysql_pool.execute("SELECT * from sesion where id_caso=%(id_caso)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_sesion': result[0], 'fecha': result[1], 'descripcion': result[2], 'id_caso': result[3]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para eliminar una sesion
    def delete_sesion(self, id_sesion):
        params = {'id_sesion' : id_sesion}      
        query = """delete from sesion where id_sesion = %(id_sesion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


################### Participante ################################

    # Funcion para agregar una participante
    def add_participante(self,nombre, ape_paterno, ape_materno, tipo, id_sesion):
        params = {
            'nombre' : nombre,
            'ape_paterno' : ape_paterno,
            'ape_materno' : ape_materno,
            'tipo' : tipo,
            'id_sesion': id_sesion
        }  
        query = """insert into participante (nombre, ape_paterno, ape_materno, tipo, id_sesion )
            values (%(nombre)s, %(ape_paterno)s, %(ape_materno)s, %(tipo)s, %(id_sesion)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id': cursor.lastrowid, 'nombre': nombre, 'ape_paterno': ape_paterno, 'ape_materno': ape_materno, 'tipo': tipo, 'id_sesion': id_sesion}
        return data

    # Funcion para obtener un participante por su ID
    def get_participante(self, id_participante):
        params = {'id_participante' : id_participante}      
        rv = self.mysql_pool.execute("SELECT * from participante where id_participante=%(id_participante)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_participante': result[0], 'nombre': result[1], 'ape_paterno': result[2], 'ape_materno': result[3], 'tipo': result[4], 'id_sesion': result[5]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los participantees
    def get_participantes(self):
        rv = self.mysql_pool.execute("SELECT * from participante")  
        data = []
        content = {}
        for result in rv:
            content = {'id_participante': result[0], 'nombre': result[1], 'ape_paterno': result[2], 'ape_materno': result[3], 'tipo': result[4], 'id_sesion': result[5]}
            data.append(content)
            content = {}
        return data
    
    #Funcion para obtener todos los participantees de una sesion especifico
    def get_participantes_sesion(self,id_sesion):
        params = {'id_sesion' : id_sesion} 
        rv = self.mysql_pool.execute("SELECT * from participante where id_sesion=%(id_sesion)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_participante': result[0], 'fecha': result[1], 'descripcion': result[2]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para eliminar una participante
    def delete_participante(self, id_participante):
        params = {'id_participante' : id_participante}      
        query = """delete from participante where id_participante = %(id_participante)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

################### declaracion ################################

    # Funcion para agregar una declaracion
    def add_declaracion(self,titulo, tipo, declaracion, id_participante):
        params = {
            'titulo' : titulo,
            'tipo' : tipo,
            'declaracion' : declaracion,
            'id_participante': id_participante
        }  
        query = """insert into declaracion (titulo, tipo, declaracion, id_participante )
            values (%(titulo)s, %(tipo)s, %(declaracion)s, %(id_participante)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id': cursor.lastrowid, 'titulo': titulo, 'tipo': tipo, 'declaracion': declaracion, 'id_participante': id_participante}
        return data

    # Funcion para obtener un declaracion por su ID
    def get_declaracion(self, id_declaracion):
        params = {'id_declaracion' : id_declaracion}      
        rv = self.mysql_pool.execute("SELECT * from declaracion where id_declaracion=%(id_declaracion)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_declaracion': result[0], 'titulo': result[1], 'tipo': result[2], 'declaracion': result[3], 'id_participante': result[4]}
            data.append(content)
            content = {}
        return data

    # Funcion para obtener todos los declaraciones
    def get_declaraciones(self):
        rv = self.mysql_pool.execute("SELECT * from declaracion")  
        data = []
        content = {}
        for result in rv:
            content = {'id_declaracion': result[0], 'titulo': result[1], 'tipo': result[2], 'declaracion': result[3], 'id_participante': result[4]}
            data.append(content)
            content = {}
        return data
    
    #Funcion para obtener todos los declaraciones de una participante especifico
    def get_declaraciones_participante(self,id_participante):
        params = {'id_participante' : id_participante} 
        rv = self.mysql_pool.execute("SELECT * from declaracion where id_participante=%(id_participante)s", params)  
        data = []
        content = {}
        for result in rv:
            content = {'id_declaracion': result[0], 'titulo': result[1], 'tipo': result[2], 'declaracion': result[3], 'id_participante': result[4]}
            data.append(content)
            content = {}
        return data
    
    # Funcion para eliminar una declaracion
    def delete_declaracion(self, id_declaracion):
        params = {'id_declaracion' : id_declaracion}      
        query = """delete from declaracion where id_declaracion = %(id_declaracion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


if __name__ == "__main__":    
    tm = TaskModel()
    #print(tm.get_actividad(1))
    #print(tm.get_actividads())
    #print(tm.delete_cliente(67))
    #print(tm.get_clientes())
    #print(tm.create_actividad('prueba 10', 'desde python')) 
