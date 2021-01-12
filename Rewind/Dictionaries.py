#Write a program that reads the words in words.txt 
# and stores them as keys in a dictionary.
#  It doesn’t matter what the values are.
#  Then you can use the in operator as a fast way to check whether a string is in the dictionary.


fhand = open('words.txt')
mydictionary = dict()
for line in fhand:
    words = line.split()
    print(words)
    for word in words:
        if word not in mydictionary:
            mydictionary[word] = 1
        else:
            mydictionary[word] += 1
print(mydictionary)
#maximum = max(mydictionary[word])
#minimum = min(mydictionary[word])
#print(minimum)
#print(maximum)
#print(mydictionary)
'''
word = 'brontosaurus'
d = dict()
for c in word:
d[c] = d.get(c,0) + 1
print(d)
'''