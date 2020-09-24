#Exercise 1: Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a
#  new list that contains all but the first and last elements.
def middle(thislist):
    del thislist[0]
    del thislist[-1]
    newlist = list()
    newlist.extend(thislist)
    print(newlist)
    return
numbers = ["elma","armut","patates","1","2","3","4"]
middle(numbers)
