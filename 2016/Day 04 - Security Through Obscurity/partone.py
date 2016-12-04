import re
import collections
from operator import itemgetter
	
def process_input(instr):
	tokens = re.findall(r"[^-\[\]]+", instr)
	str = ''.join(tokens[0:len(tokens)-2])
	count = collections.Counter(str)
	count = list(count.items())
	sortct = sorted(count, key=lambda x:(-x[1],x[0]))

	for k in range(5):
		if sortct[k][0] != tokens[len(tokens)-1][k]:
			return 0
	
	roomname = re.split(r"(-\d+)[^\s]*", instr)
	shift = int(tokens[len(tokens)-2]) % 26
	newname = ""
	for c in roomname[0]:
		if c == '-':
			newname += " "
		else:
			newname += chr(((ord(c) - ord('a')) + shift) % 26 + ord('a'))			
	print(newname + ' ' + tokens[len(tokens)-2])
	return int(tokens[len(tokens)-2])
	
inFile = open('input.txt','r')
instruction_list = [inLine.rstrip('\n') for inLine in inFile]

sum_of_ids = 0
for instr in instruction_list:
	sum_of_ids += process_input(instr)

print (sum_of_ids)
#for token in tokens:
#	print(token)
input("Press Enter to continue...")