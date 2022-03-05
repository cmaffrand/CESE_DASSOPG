import ast

def getconfig2dic(name):
    dic = {}
    try:
        f = open(name, mode='r', encoding = 'utf-8')
        contents = f.read()
        dic = ast.literal_eval(contents)
    finally:
        f.close()
    return dic
   
diccionario = getconfig2dic("config.txt")
print(diccionario)