newDict=dict()
fname=input('enter your file name ')
if len(fname)<1 : fname='mbox-short.txt'
try:
    handle=open(fname)
except:
    print('File cannot be opened', fname)
    exit()
for line in handle:
    words=line.split()
    if len(words)==0 or len(words)<2  or words[0]!='From' :
        continue
    else:
        colon=words[5].find(':')
        hour=words[5][:colon]
        if hour not in newDict:
            newDict[hour]=1
        else:
            newDict[hour]+=1
lst=list()
for key, value in list(newDict.items()) :
    lst.append((key,value))
lst.sort()
for key, value in lst:
    print(key, value)
