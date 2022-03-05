import os

ttylist = []
ttyroutelist = []

cmdOut = os.popen('df -h').read()
#print(cmdOut)

lineOut = cmdOut.split("\n")
#print(lineOut)
for index,text in enumerate(lineOut):
    tempLine = text.split(" ")
    #print(tempLine)
    ttylist.append(tempLine[0])
    ttyroutelist.append(tempLine[len(tempLine)-1])
del ttylist[0]
del ttyroutelist[0]
print(ttylist)
print(ttyroutelist)