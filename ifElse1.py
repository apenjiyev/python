hrs = input("Enter Hours:")
hours = float(hrs)
r=input('enter rate')
rate=float(r)
if hours>40:
    reg=rate*hours
    otp=(hours-40)*(rate*0.50)
    pay=reg+otp
    print(pay)
else:
    pay=hours*rate
    print(pay)
