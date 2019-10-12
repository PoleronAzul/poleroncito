from model.controladorP import Personas

class controladorN:
    def __init__(self):
        self.id = 0
    def getIncrementar(self)->int:
        self.id = self.id +1
        return self.id

    def aggregarNotaP(self,Personas:Personas):
        newDescrip = input("ingrese la descripcion de la nota: ").lstrip
        newNota = Nota(newDescrip)
        newNota.id = self.getIncrementar()
        Personas.notas.append(newNota)
        print("Nota agregada correctamente")
        wait()

    def listarNota(self,persona:Personas):
        if len(personas.notas)>0:
            for nota in persona.notas:
                nota.printInformation()
        else:
            print("No hay notas en el sistema")
        wait()
    
    def findId(self,id:int,persona:Personas)->Nota:
        if self.countNota(persona)>0:
            for nota in persona.notas:
                if int(nota.id) == id:
                    return nota
        return None

        def modificarNota(self,persona:Personas)->Nota:
            if self.countNota(persona)>0:
                idNot = input("ingrese la Id de la nota: ")
                while not(idNota.isnumeric()) or idNote==" ":
                    idNota = input("ID no valida, por favor intentelo nuevamente")
                    if idNota == "":
                        return
                    elif idNota.isnumeric():
                        notaFound = self.findId(int(idNota),persona)
                newDescrip = input ("ingrese la descripcion de la nota: ")
                if newDescrip == "":
                    newDescrip = notaFound.desNota
                if newDescrip == notaFound.desNota:
                    print("los datos son los mimos que antes")
                else:
                    notaFound.desNota = newDescrip
                    print("Nota modificada correctamente. ")
            else:
                print("No existen registro de notas")
            wait()
        
        def eliminarNota(self, persona:Personas):
            if self.countNota(persona)>0:
                idNota = input("ingrese ID de la nota a eliminar")
                if not(idNota.isnumeric()) or idNota == "":
                    print("ID no valida, favor intentelo nuevamente")
                    idNota = input("Ingrese ID de la nota a eliminar: ").lstrip
                findNota = self.findId(int(idNota),persona)
                while findNota == None:
                    idNota = input("La ID ingresada no es valida intentelo nuevamente")
                    if idNota = input == "":
                        return
                    elif idNota.isnumeric():
                            findNota = self.findId(int(idNota),persona)
                pos = persona.nota.index(findNota) 
                persona.nota.pop(pos)
                print("nota eliminada")
            else:
                print("no existen notas registrdas en el sistema")
            wait()

        def contarNota(self,persona:Personas)->int:
            return len(persona.nota)       
