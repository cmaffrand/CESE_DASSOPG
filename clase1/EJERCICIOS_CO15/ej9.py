import myconfig
from datetime import datetime

orgname = "orgconfig.txt"
modname = "modconfig.txt"
dconfig = {}
actual_time = datetime.now()
hora_min = actual_time.strftime("%H:%M")
print(hora_min)

dconfig = myconfig.getconfig2dic(orgname)
print(dconfig)
dconfig["backup"] = hora_min
print(dconfig)

myconfig.newconfigfromdic(dconfig,modname)