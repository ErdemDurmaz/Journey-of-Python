filehandler = open('mbox-short.txt')
count = 0
summary= 0
for line in filehandler:
    if line.startswith('X-DSPAM-Confidence'):
        count += 1
        var = float(line[20:])
        summary = summary + var
avarage = summary / count
print('Avarage of the the file',avarage)