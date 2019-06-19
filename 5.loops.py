a=[]
while True:
    ask=input('give me a number ')
    if ask=="done":
        break
    try:
        number=int(ask)
    except:
        print('Invalid input')
        continue
    b=number
    a.append(b)
a.sort()
print('Maximum is',max(a))
print('Minimum is',min(a))
