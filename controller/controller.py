from model.model import Model
from view.view import View

class Controller:
    #CONSTRUCTOR
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contacto controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo , dir):
        e, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo , dir)
        if e:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre='', n_tel='', n_correo='', n_dir=''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)

    #Cita controllers
    def agregar_cita(self, id_cita,id_contacto, lugar, fecha, hora , asunto):
        e, c = self.model.agregar_cita(id_cita,id_contacto, lugar, fecha, hora , asunto)
        if e:
            self.view.agregar_cita(c)
        else:
            self.view.cita_ya_existe(c)
    
    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)
    
    def leer_todos_citas(self):
        c = self.model.leer_todos_citas()
        self.view.mostrar_citas(c)
    
    
    def actualizar_cita(self, id_cita,n_id_contacto='', n_lugar='', n_fecha='', n_hora='' , n_asunto=''):
        e = self.model.actualizar_cita(id_cita,n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)
        if e:
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)
    
    def borrar_cita(self, id_cita):
        e, c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_citas_letra(self, letra):
        c = self.model.leer_citas_letra(letra)
        self.view.mostrar_citas(c)

    #General methods
    def insertar_contactos(self):
        self.agregar_contacto(1,'Juan Perez', '4641661118', 'jperez@gmail.com','Av siempre viva 113')
        self.agregar_contacto(2,'Carlos Martinez', '6473350', 'carlos.martinez@gmail.com','Cerro Azul 201')
        self.agregar_contacto(3,'Armando Navarro', '6473350', 'carlos.martinez@gmail.com','Cerro Azul 201')
    
    def insertar_citas(self):
        self.agregar_cita(1,1, 'Cerveceria Chapultepec', '26/05/20','14:30','Tomar')
        self.agregar_cita(2,1, 'MCarty´s', '26/05/20','14:30','Tomar')
        self.agregar_cita(3,2, 'MCarty´s', '26/05/20','14:30','Tomar')

    def start(self):
        #print("esto es un ejemplo de vista sencillo")
        self.view.start()
        #Insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        #Show all contacts in BD
        self.leer_todos_contactos()
        self.leer_todos_citas()
        self.leer_contactos_letra('A')
        self.leer_citas_letra('C')
        self.menu()
        

    def menu(self):
        #Display menu
        self.view.menu()
        while True:
            self.view.menu()
            o = input('Selecciona una opcion (1-9):')
            
            #Agregar contacto
            if o =='1':
                id_contacto = int(input('ID del contacto:'))
                nombre = input('Nombre: ')
                tel = input('Telefono: ')
                correo = input('Correo: ')
                dir = input('Direccion ')
                self.agregar_contacto(id_contacto,nombre,tel,correo,dir)
                

            #Buscar contacto
            elif o=='2':
                id_contacto = int(input('id del contacto que desea mostrar:'))
                self.leer_contacto(id_contacto)
            #Actualizar contacto
            elif o=='3':
                id_contacto = int(input('ID del contacto:'))
                nombre = input('Nombre: ')
                tel = input('Telefono: ')
                correo = input('Correo: ')
                dir = input('Direccion ')
                self.actualizar_contacto(id_contacto,nombre,tel,correo,dir)
                
            #Borrar contacto
            elif o=='4':
                id_contacto = int(input('id del contacto que desea borrar: '))
                self.borrar_contacto(id_contacto)
                

            #Agregar cita
            elif o=='5':
                id_cita = int(input('ID de la cita:'))
                id_contacto = int(input('ID del contacto:'))
                lugar = input('Lugar: ')
                fecha = input('Fecha: ')
                hora = input('Hora: ')
                asunto = input('Asunto: ')
                self.agregar_cita(id_cita,id_contacto,lugar,fecha,hora,asunto)
                
                
            #Mostrar cita
            elif o=='6':
                id_cita = int(input('id de la cita que desea mostrar:'))
                self.leer_cita(id_cita)

            #Actualizar cita
            elif o=='7':
                id_cita = int(input('ID de la cita:'))
                id_contacto = int(input('ID del contacto:'))
                lugar = input('Lugar: ')
                fecha = input('Fecha: ')
                hora = input('Hora: ')
                asunto = input('Asunto: ')
                self.actualizar_cita(id_cita,id_contacto,lugar,fecha,hora,asunto)

            #Borrar cita
            elif o=='8':
                id_cita = int(input('id de la cita que desea borrar: '))
                self.borrar_cita(id_cita)
                break

            #Mostrat todos los contactos
            elif o=='9':
                self.leer_todos_contactos()

            elif o=='10':
                break
                
            else:
                self.view.opcion_no_valida()
                