#Rewrite the program that prompts the user for a list of numbers and prints out 
# the maximum and minimum of the numbers at the end when the user enters “done”.
#  Write the program to store the numbers the user enters in a list and use the max() and min()
#  functions to compute the maximum and minimum numbers after the loop completes.
my_numbers = []
while True:
    str_value = input("Enter a number: ")
    if str_value == 'done':
        break
    my_numbers.append(str_value)
    print(my_numbers)
minimum_number = min(my_numbers)
maximum_number = max(my_numbers)
print("The lowest number is" ,minimum_number)
print("The highest numbers is",maximum_number)