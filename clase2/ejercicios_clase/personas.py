
class Persona:
    """docstring for Persona."""
    def __init__(self, nombre="", edad=0):
        #self.__nombre = nombre
        #self.__edad = edad
        self.set_nombre(nombre)
        self.set_edad(edad)
        
    def set_nombre(self, nombre):
        if nombre!="":
            self.__nombre = nombre
    
    def set_edad(self, edad):
        if edad > 0 and edad < 125:
            self.__edad = edad
            
    def get_nomnbre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def print_persona(self):
        print(self)
        print(self.__dict__)
        print(f"{self.get_nomnbre()} {self.get_edad()}")
        
    def es_mayor_de_edad(self):
        if self.get_edad() >= 18:
            return True
        else:
            return False
        
    def es_mayor_que(self, persona):
        if self.get_edad() > persona.get_edad():
            return True
        else:
            return False
        
    @staticmethod
    def dump_csv(name,lista):
        with open(name,"w",encoding="utf-8") as f:
            f.write("Nombre,Edad\n")
            for per in lista:
                linea = f"{per.get_nomnbre()},{per.get_edad()}\n"
                f.write(linea)

    

    