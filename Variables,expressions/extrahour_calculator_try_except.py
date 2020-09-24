

hours = input('Enter Hours ')
rate = input('Enter rate ')

try:
    fhour = float(hours)
    frate = float(rate)
except:
    print("error")
    quit()

if fhour > 40 :
    print("overtime")
    reg = fhour * frate
    otp = (fhour - 40.0)
    extra = frate * 1.5
    sum_otp = otp * extra
    total_sum = reg + sum_otp
    print(total_sum)
else:
    reg = fhour * frate
    print("Regular",reg)
