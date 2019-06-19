def computepay(hours, rate):
    if hours>40:
        reg=rate*hours
        otp=(hours-40)*(rate*0.50)
        pay=reg+otp
    else:
        pay=hours*rate
    print(pay)
    return pay
f =input('hours?')
g=input('rate?')
h=float(f)
j=float(g)
computepay(h, j)
