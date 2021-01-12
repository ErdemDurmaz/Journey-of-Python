#Gross Pay Calculator 1.5 times the hourly rate above 40


def computepay(hourinp,rateinp):
  #  
    if hourinp > 40:
        pay = (hourinp - 40)* rateinp * 1.5 + (40 * rateinp)
    else:
        pay = (hourinp*rateinp)
    return pay

hourinp = int(input("Please enter the Hours "))
rateinp = float(input("Please enter the rate "))
pay = computepay(hourinp,rateinp)
print("pay",pay)