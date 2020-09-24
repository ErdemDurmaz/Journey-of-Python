#Erdem Durmaz Avarage Calculator
minimum = None
count = 1
while True:
    line = (input('Enter a number: '))
    if line == 'done':
        break
    
    try:
        line = float(line)
  
    except:
        print('invalid input')
        continue 
  
    if minimum is None:
        line = minimum
   
    elif minimum < line:
        minimum = line
        break
    print(minimum)
         
