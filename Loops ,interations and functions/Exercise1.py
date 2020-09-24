#Erdem Durmaz Avarage Calculator
sum = None
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
    if sum is None:
        sum = line
    else:   
            count = count +1 
            sum = (sum) + (line)
            sum = sum / count
print(sum)     
