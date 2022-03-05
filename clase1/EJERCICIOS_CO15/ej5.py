
def stringRepalce(string,char):
    
    list = [0]    
    for index,charinstring in enumerate(string):
        if " " == charinstring:
            list.append(index)
       
    if len(list) == 1:
        return string
    else:
        list.append(len(string))
    #print(list)
    
    for index,poslist in enumerate(list):
        if index == 0:
            outstring = string[poslist:list[index+1]] + char
        elif len(list) == index+1:
            return outstring
        elif len(list) == index+2:
            outstring = outstring + string[poslist+1:list[index+1]]
        else:
            outstring = outstring + string[poslist+1:list[index+1]] + char
             
str = input("Ingrese un string: ")
print(stringRepalce(str,"_"))