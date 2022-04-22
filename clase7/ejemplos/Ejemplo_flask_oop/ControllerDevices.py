
import json
from DeviceDAO import DeviceDAO
from Device import Device

class ControllerDevices:
    
    def __init__(self,app,request,db):
        self.app = app
        self.request = request
        self.db = db
        
    def getAll(self):
        devDAO = DeviceDAO(self.db)
        d = devDAO.getAll()
        return json.dumps(d, default=Device.objToDict)
    
    def getSome(self,page,size):
        devDAO = DeviceDAO(self.db)
        d = devDAO.getSome(page,size)
        return json.dumps(d, default=Device.objToDict)
    
    def setSome(self,devId,value):
        devDAO = DeviceDAO(self.db)
        return devDAO.setSome(devId,value)