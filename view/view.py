class View:
    def mostrar_contacto(self, contacto):
        print('**************** Datos del contacto **************** ')
        print('Nombre', contacto.nombre)
        print('Telefono', contacto.tel)
        print('Correo', contacto.correo)
        print('direccion', contacto.dir)
        print('******************************** ')

    def mostrar_contactos(self, contactos):
        print('**************** Contactos **************** ')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('******************************** ')

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha agregado a la base de datos!')

    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha borrado de la base de datos!')

    def actualizar_contacto(self, id_contacto):
        print(id_contacto,'Se ha modificado correctamente')

    def contacto_ya_existe(self, contacto):
        print('El CONTACTO', contacto.id_contacto,'Contacto ya existe en la base de datos')

    def contacto_no_existe(self,id_contacto):
        print(id_contacto,'Contacto no existe en la base de datos')

    def start(Self):
        print("esto es un ejemplo de vista sencillo")
    def end(self):
        print("Hata la vista!")

    def mostrar_cita(self, cita):
            print('**************** Datos de la cita **************** ')
            print('Lugar', cita.lugar)
            print('Fecha', cita.fecha)
            print('Hora', cita.hora)
            print('Asunto', cita.asunto)
            print('******************************** ')
    def mostrar_citas(self, citas):
        print('**************** Citas **************** ')
        for c in citas:
            print(c.id_cita, c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
        print('******************************** ')
    def agregar_cita(self, cita):
        print(cita.lugar, 'Se ha agregado a la base de datos!')

    def borrar_cita(self, cita):
        print(cita.asunto, 'Se ha borrado de la base de datos!')
        
    def actualizar_cita(self, id_cita):
        print(id_cita, 'Se ha modificado')
    def cita_ya_existe(self,cita):
        print(cita.id_cita, 'Cita ya existe en la base de datos')
    def cita_no_existe(self,id_cita):
        print(id_cita,'Cita no existe en la base de datos')
    #GENERAL VIEWS
    def start(Self):
        print("esto es un ejemplo de vista sencillo")
    def end(self):
        print("Hata la vista!")
    def menu(self):
        print('1. Agregar contacto')
        print('2. Buscar contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Agregar cita')
        print('6. Buscar cita')
        print('7. Actualizar cita')
        print('8. Borrar cita')
        print('9. Mostrar todos los contactos')
        print('10. Terminar')