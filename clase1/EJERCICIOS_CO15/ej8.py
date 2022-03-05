
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
        
diccionario = dict(zip('abcd',[1,2,3,4]))
#print(diccionario)
#print(len(diccionario))
name = "Dic.txt"

newconfigfromdic(diccionario,name)

