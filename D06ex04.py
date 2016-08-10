import os

def read_roster():
	with open('roster.txt', 'r') as f:
                eRoster = []
                line = f.readline()
                count = 0

                for line in f:
                        firstname = line.split()
                        if 'e' in firstname[0] or 'E' in firstname[0]:
                                count += 1
                                eRoster.append(firstname[0])
	
	with open('newroster.txt', 'w') as g:
                g.write('The number of names containing the letter "e" is '+ str(count) + '\n'*2)
                g.write(str(', '.join(eRoster)))

read_roster()
