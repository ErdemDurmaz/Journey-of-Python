index = 5
fruit = 'banana'
while index <= len(fruit):
    letter = fruit[-index]
    print(letter)
    index -= 1
    if index == (-1):
        quit()