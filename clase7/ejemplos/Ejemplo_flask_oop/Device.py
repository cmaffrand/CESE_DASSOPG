

class Device:
    
    def __init__(self,id_dev,name,ip,status):
        self.id_dev = id_dev
        self.name = name
        self.ip = ip
        self.status = status
        
    @staticmethod
    def objToDict(obj):
        return {"id_dev":obj.id_dev,"name":obj.name,"ip":obj.ip,"status":obj.status}