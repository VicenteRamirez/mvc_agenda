from .contacto import Contacto
from .cita import cita

class Model: 

    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id_contacto(self,id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True,c
        return False, 0

    def esta_id_cita(self,id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True,c
        return False, 0

    #Contacto methods
    def agregar_contacto(self,id_contacto, nombre, tel, correo , dir):
        e, c = self.esta_id_contacto(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre, tel, correo , dir)
            self.contactos.append(c)
            return True, c
        return False, c

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id_contacto(id_contacto)
        return e, c

    def actualizar_contacto(self,id_contacto,n_nombre, n_tel, n_correo, n_dir):
        e, c = self.esta_id_contacto(id_contacto)
        if e:
            if n_nombre != '':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel  = n_tel
            if n_correo != '':    
                c.correo = n_correo
            if n_dir != '':
                c.dir = n_dir
            return True
        return False

    def borrar_contacto(self,id_contacto):
        e, contacto = self.esta_id_contacto(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                    self.citas.remove(c)
            return True, contacto
        return False

    #Cita method
    def agregar_cita(self,id_cita,id_contacto, lugar, fecha, hora , asunto):
        e, c = self.esta_id_cita(id_cita)
        if not e:
            c = cita(id_cita,id_contacto, lugar, fecha, hora , asunto)
            self.citas.append(c)
            return True, c
        return False, c
            #print("Contacto no existe")

    def leer_cita(self, id_cita):
        e, c = self.esta_id_cita(id_cita)
        return e, c
    def actualizar_cita(self,id_cita,n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, c = self.esta_id_cita(id_cita)
        if e:
            if n_id_contacto != '':
                c.id_contacto = n_id_contacto
            if n_lugar != '':
                c.lugar = n_lugar
            if n_fecha != '':
                c.fecha = n_fecha
            if n_hora != '':
                c.hora = n_hora
            if n_asunto != '':
                c.asunto = n_asunto
        return False        
    def borrar_cita(self,id_cita):
        e, c = self.esta_id_cita(id_cita)
        if e:
            self.citas.remove(c)
            return True, c
        return False, 0
        
   
    def leer_contactos_letra(self,letra):
        cont = []
        for c in self.contactos:
            if letra == c.nombre[0] :
                cont.append(c)
        return cont
    def leer_citas_letra(self,letra):
        cont = []
        for c in self.citas:
            if letra == c.lugar[0] :
                cont.append(c)
        return cont

    def cita_fecha(self,fec):
        fech = []
        for c in self.citas:
            if fec == c.fecha :
                fech.append(c)
        return fech
        
    def leer_todos_contactos(self):
        return self.contactos
    
    def leer_todos_citas(self):
        return self.citas

    def leer_contacto_letra(self, letra):
        lista = [c for c in self.contactos if c.nombre[0].lower() == letra.lower()]
        """lista = []
        for c in self.contactos:
            if c.nombre[0].lower() == letra.lower():
                lista.append(c)
                """
        return lista
    def borrar_contacto_cita(self,id_contacto):
        e, c = self.esta_id_contacto(id_contacto)
        if e:
            self.contactos.remove(c)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                    self.citas.remove(c)
            return True
        return False

