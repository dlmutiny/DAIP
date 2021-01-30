import csv
r = csv.reader(file(r'example_yosemite_temps.csv'))
w = csv.writer(file(r'testParse.csv', 'w'))
for line in r:
#    if line[0] in ['8','10']: # look for the data in lines 8 and 10
#        w.writerow(line)
    if line[0] in ['4214','4215','4216'] <= 7: # look for the data in lines 8 and 10
        w.writerow(line)
