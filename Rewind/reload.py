'''
Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35 
Enter Rate: 2.75 

Pay: 96.25
'''
hours = input('Prompt hours ')
rate = input('Prompt rate ')
sum =(int(hours) * float(rate))
print("Your gross pay is", sum)