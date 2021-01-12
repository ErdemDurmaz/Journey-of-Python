try:
    grade = float(input("Enter score: "))
except:
    print("Bad score")
    quit()

if grade < 0 or grade > 1.0:
    print("Score is out of range!")
elif grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
    print("F")