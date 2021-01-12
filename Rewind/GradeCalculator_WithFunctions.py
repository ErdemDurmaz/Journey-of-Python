#Grade Calculator
def gradecalculator(inpscore):
    if inpscore > 1.0:
        print("Wrong input0")
        quit()
    elif inpscore < 0.0:
        print("Wrong input1")
        quit()
    if inpscore >= 0.9:
        print("A")
    elif inpscore >= 0.8:
        print("B")
    elif inpscore >= 0.7:
        print("C")
    elif inpscore >= 0.6:
        print("D")
    elif inpscore < 0.6:
        print("F")
    else:
        quit()
inpscore = float(input("Prompt for score between 1.0 and 0.0:  "))
total = gradecalculator(inpscore)
print(total)
