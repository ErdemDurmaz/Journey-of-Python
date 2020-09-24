filehandler = open('mbox-short.txt')
count = 1
summary= 0
for line in filehandler:
    if line.startswith('X-DSPAM-Confidence'):
        count = count + 1
        count = int(count)

        floats = (line[20:])
        floats = float(floats)
        summary = float(summary)
       
        summary = summary + floats
        avarage = summary / count
print('Average spam confidence',avarage)
           


