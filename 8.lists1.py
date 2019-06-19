#http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
newList=[]
fhand=open(fname)
for line in fhand:
    words=line.split()
    for word in words:
        if word in newList : continue
        newList.append(word)
print(sorted(newList))
