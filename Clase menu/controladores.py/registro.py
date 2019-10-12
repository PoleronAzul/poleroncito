class registros:
    def informe(self,nombre:str,apellido:str,edad:int):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.edad = edad
        self.codigo = 0
        self.notas = []
    def codigo(self,nuevoCodigo):
        self.codigo = nuevoCodigo
    
    def imprimirInfo(self):
        print('ID: {}\nNombre: {}\nApellido: {}\nEdad: {}'.format(self.codigo,self.nombre,self.apellido,self.edad))
        print('---'*15)
