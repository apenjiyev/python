fname=input('enter your file name ')
fhand=open(fname)
counts=dict()
for line in fhand:
    words=line.split()
    if len(words)==0 or len(words)<2 or words[0]!='From':
        continue
    else:
        if words[1] not in counts:
            counts[words[1]]=1
        else:
            counts[words[1]]+=1
            
maximum=0

for count in counts:
    if counts[count]>maximum:
        maximum=counts[count]
        maximum_address=count
print(maximum_address, maximum)
