import ej3_1

s_in = input("Ingrese tiempo en formato s: ")
hms = ej3_1.s2hms(int(s_in))
print(f"Tiempo en formato hms: {hms[0]}:{hms[1]}:{hms[2]}")
hms_in = input("Ingrese tiempo en formato hms: ")
h = int(hms_in[0:hms_in.find(":")])
m = int(hms_in[hms_in.find(":")+1:hms_in.rfind(":")])
s = int(hms_in[hms_in.rfind(":")+1:len(hms_in)])
print(f"Tiempo en formato s: {ej3_1.hms2s(h,m,s)}")