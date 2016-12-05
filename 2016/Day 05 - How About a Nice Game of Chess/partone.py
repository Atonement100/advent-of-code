import hashlib

def print_hacker_string(confirmed, fullstr):
	conf = confirmed.copy()
	for k in range(len(conf)):
		if conf[k] == "|":
			conf[k] = fullstr[k]
	print(''.join(conf))
		

def process_input(instr):
	confirmed = ['|', '|', '|', '|', '|', '|', '|', '|']
	i = 0
	for k in range(8):
		while True:
			string = hashlib.md5((instr + str(i)).encode()).hexdigest()[0:8]
			if i % 10000 == 0:
				print_hacker_string(confirmed, string)
			#print(confirmed)
			i += 1
			if string[0:5] == "00000":
				if string[5].isdigit() and int(string[5]) < 8 and confirmed[int(string[5])] == "|":
					break
		confirmed[int(string[5])] = string[6]
	print(''.join(confirmed))
	
input = "ugkcyxxp"
process_input(input)
