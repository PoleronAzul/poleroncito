from controladores.registro import registros

class ingresar:

    def __init__(self):
        self.Personas = []
        self.count = 0
    
    def newPersona(self):
        newNombre = input("Ingrese su nombre: ").lstrip()
        newApellido = input("Ingrese su apellido: ").lstrip()
        newEdad = input("Ingrese su edad: ").lstrip()

        while not(newEdad.isnumeric()):
            print("Por favor ingrese nuevamente su edad".format(anio))
            anio = imput("Ingrese su edad: ")
        if self.findNombre(newNombre, apellido) ==None:
            newPersona = persona(newNombre,newApellido,newEdad)
            newPersona.setCod(self.getCount())
            self.Personas.append(newPersona)
            print("Se agrego correctamente")
            else:
                print("No se a podido agregar, por favor vuelve a intentar")
            wait()
    
    def getCount(self)->int:
        self.count = self.count+1
        return self.count
    
    def findNombre(self,nombre:str,apellido:str)->Personas:
        for per in self.Personas:
            if per.nombre.lower() == nombre.lower() and per.apellido.lower() = apellido.lower():
                return per
        return None
    
    def findId(self,cod:int)->Personas:
        for per in self.Personas:
            if int(per.cod) == cod:
                return per
        return None
    
    def getPersonas(self):
        in len(self.Personas)==0
        print("No hay persona registradas")
        for per in self.Personas:
            per.printInformation()
        wait()
    
    def borrarPersonasId(self)
    if self.countPersonas()>0:
        id = input("ingrese el id de la persona que desea eliminar: ")
        while not(id.isnumeric())
            print("Error, favor ingresar nuevamente el id".format(id))
            id =  input("Ingree la ID de la persona que desea eliminar")
        find = self.findId(int(id))
        if find != None:
            pos = self.Personas.index(find)
            self.Personas.pop(pos)
            print("Personas eliminada correctamente")
        else:
            print("El id ingresado no se encuentra en el sistema")
    else:
        print("No existen personas registradas.")
    wait()

    def modifPersonas(self):
        if self.countPersonas()>0:
            id = input("Ingrese ID de la persona que desea modificar")
            while not(id.isnumeric()):
                print("Error, favor intentelo nuevamente.".format(id))
                id = input("Ingrese ID de la persona que desea modificar")
                find = self.findId(int(id))
                if(find != None):
                    newNombre = input("Ingrese su nombre ({}) :".format(findNombre)).lstrip()
                    if newNombre == " ":
                        newNombre = findNombre
                    newApellido = input("Ingrese su apellido ({}) :".format(findApellido)).lstrip()
                    if newApellido == " ":
                        newApellido = find.apellido
                    newEdad = input("Ingrese su edad ({}) : ".format(str(find.edad))).lstrip()
                    if newEdad == " ":
                        newEdad = find.edad
                    
                    while not(newEdad.isnumeric()):
                        print("Por favor intentelo nuevamente".format(newEdad))
                        newEdad = input("Ingrese su edad ({}) : ".format(str(find.edad))).lstrip()
                    if find.nombre.lower() == newNombre.lower() and find.apellido.lower() == newApellido.lower() and int(find.edad) == int(newEdad):
                    else:
                        find.nombre = newNombre
                        find.apellido = newApellido
                        find.edad = int(newEdad)
                        print("Cambios guardados exitosamente.")
                else:
                    print("La ID ingresada no se encuentra registrada"
            else:
                print("No hay personas registradas")
            wait()
    
    def contarRegis(self,registros)->int:
        return len(self.registros)