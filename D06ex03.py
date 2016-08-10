import os

def read_roster():
	f = open('roster.txt', 'r')
	eRoster = []
	line = f.readline()
	count = 0

	for line in f:
		firstname = line.split()
		if 'e' in firstname[0] or 'E' in firstname[0]:
			count += 1
			eRoster.append(firstname[0])
	f.close()
	print('The number of names containing the letter "e" is', count)
	print(', '.join(eRoster))

read_roster()
