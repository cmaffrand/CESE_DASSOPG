
class Sensor:
    """docstring for Sensor."""    
    def __init__(self, num):
        self.set_num(num)
        self.__value = 0.0
        
    def set_num(self, num):
        if num >= 0:
            self.__num = num

    
    def read_file(self,path):
        with open(path,"r",encoding="utf-8") as f:
            self.__value = float(f.read())
        return self.__value
    
    def get_num(self):
        return self.__num
    
    def get_value(self):
        self.__value = "No value"
        print("Warning: Clase sin metodo get_value()")
        return self.__value
    
class SensorTemperatura(Sensor):
    """docstring for SensorTemperatura.""" 
    def __init__(self, num):
        super().__init__(num)
        
    def get_value(self):
        temp = float(self.read_file(f"tmp/temp{self.get_num()}.data"))
        if temp < 0:
            self.__value = 0.0
        else:
            self.__value = temp
        return self.__value
    
class SensorHumedad(Sensor):
    """docstring for SensorHumedad.""" 
    def __init__(self, num):
        super().__init__(num)
        
    def get_value(self):
        temp = float(self.read_file(f"tmp/hum{self.get_num()}.data"))
        self.__value = temp/10
        return self.__value
    
class SensorPresion(Sensor):
    """docstring for SensorPresion.""" 
    def __init__(self, num):
        super().__init__(num)     

    