from sensores import Sensor, SensorHumedad, SensorPresion, SensorTemperatura

s1 = SensorTemperatura(0)
print(f"Temperatura Leída Sensor {s1.get_num()} = {s1.get_value()}")

s2 = SensorTemperatura(1)
print(f"Temperatura Leída Sensor {s2.get_num()} = {s2.get_value()}")

s3 = SensorHumedad(0)
print(f"Humedad Leída Sensor {s3.get_num()} = {s3.get_value()}")

s4 = SensorPresion(0)
print(f"Presion Leída Sensor {s4.get_num()} = {s4.get_value()}")