#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
username = input("Please enter your name: ")
userage = int(input("Please enter your age: "))
yearsleft = (100 - userage)
calculatedyear = (2020 + yearsleft)
print("Hello ", username,"You are gonna be 100 years old in year ", calculatedyear)
