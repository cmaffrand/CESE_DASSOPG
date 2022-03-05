import ast

def newconfigfromdic(dic,name):    
    try:
        f = open(name,"w")
        f.write("{")
        for index,key in enumerate(dic):
            f.write(str(key) + ":" + str(dic[key]))
            if len(dic) == index+1:
                f.write("}\n")
            else:
                f.write(",\n")
    finally:
        f.close()
        
def getconfig2dic(name):
    dic = {}
    try:
        f = open(name, mode='r', encoding = 'utf-8')
        contents = f.read()
        dic = ast.literal_eval(contents)
    finally:
        f.close()
    return dic