
tupleList = []
tupleList.append(("Name", "Address","Age"))
tupleList.append(("George", "4312 Abbey Road",22))
tupleList.append(("John", "54 Love Ave",21))


print(tupleList)

f = open("tupleList.txt","w")
for indexlist,poslist in enumerate(tupleList):
    for indextuple,postuple in enumerate(tupleList[indexlist]):
        f.write(str(tupleList[indexlist][indextuple]))
        if len(tupleList[indexlist]) == indextuple+1:
            f.write("\n")
        else:
            f.write(",")
f.close()