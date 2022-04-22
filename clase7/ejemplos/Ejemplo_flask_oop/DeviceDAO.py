from Device import Device

class DeviceDAO:
    
    def __init__(self,db):
        self.db = db
    
    def getAll(self):
        c = self.db.cursor()
        c.execute("SELECT id,name,ip,status FROM Devices")
        
        ldevice = []
        for row in c:
            dev = Device(row[0],row[1],row[2],row[3])
            ldevice.append(dev)
        
        c.close()
        return ldevice
    
    def getSome(self,page,size):
        """Pagination of the list of devices

        Args:
            page (str): page number
            size (str): number of elements per page

        Returns:
            str: list of devices in that particular page
        """
        c = self.db.cursor()
        c.execute("SELECT id,name,ip,status FROM Devices WHERE id>=? LIMIT ?",(page,size))
        
        ldevice = []
        for row in c:
            dev = Device(row[0],row[1],row[2],row[3])
            ldevice.append(dev)
        
        c.close()
        return ldevice
    
    def setSome(self,devId,value):
        """Set the status of a device

        Args:
            devId (str): device id
            value (str): status of the device

        Returns:
            str: status of the device
        """
        status = 200
        if value != "0":
            value = "1"
        try:
            c = self.db.cursor()
            c.execute("UPDATE Devices SET status=? WHERE id=?",(value,devId))
            self.db.commit()
        except Exception as e:
            print(e)
            status = 405
        c.close()
        return status