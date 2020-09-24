filehandler = open('mbox-short.txt')

for line in filehandler:
    line = line.strip()
    if not line.startswith('From'): continue
    line = line.split()
    print(line[1])