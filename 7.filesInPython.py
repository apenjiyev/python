# Use the file name mbox-short.txt as the file name
# http://www.py4e.com/code3/mbox-short.txt
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print('File can not be opened', fname)
    exit()
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1
        numberFind=line.find(':')
        numberStrip=line[numberFind+1 : ].strip()
        convert=float(numberStrip)
        total= total+convert
        
average=total/count

print("Average spam confidence:", average)
