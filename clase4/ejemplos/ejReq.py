import requests

#https://www.mocky.io/

#URL = "http://localhost:8080/cgi-bin/index.py"
#URL = "http://www.mocky.io/v2/5d797547320000600034ea2b"
URL = "http://www.google.com"

r = requests.get(url = URL) 

if r.status_code==200: # 200 es que la respuesta fue correcta
    print(r.text)
    print(r.status_code)
else:
    print("error code:"+str(r.status_code))

