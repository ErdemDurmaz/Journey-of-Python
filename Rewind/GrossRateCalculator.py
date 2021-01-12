#Gross Pay Calculator 1.5 times the hourly rate above 40
hourinp = input("Please enter the Hours ")
rateinp = input("Please enter the rate ")


hours_overworked = (int(hourinp) - 40) #5

rawhours = float(hourinp) - hours_overworked #45- 5 = 40

subtotal = float(rawhours) * float(rateinp) #400

ratemult = float(hours_overworked) * 1.5 #5*1.5 - 7,5

ratesubtotal = float(ratemult) * float(rateinp)

total = ratesubtotal + subtotal
print(total)
