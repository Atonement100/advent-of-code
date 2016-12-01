def direction_split(str):
	direction = str.rstrip('0123456789')
	distance = str[len(direction):]
	return direction, distance
	
def process_directions(dir_tuples):
	direction = 0
	towards_east = 0
	towards_north = 0
	visited = []
	for dir in dir_tuples:
		if dir[0] == 'R':
			direction = (direction + 1) % 4
		else:
			direction = (direction - 1) % 4
			
			
		#Instead of looking at this please close this file and go anywhere else :)
		#At this point I'm too pressed for time with an exam tonight to conjure a more elegant solution
		#And too new to python to know the facilities to make it instantly more elegant 
		if direction == 0:
			for dist in range(1,int(dir[1]) + 1):
				if (towards_north + dist, towards_east) in visited:
					return towards_north + dist, towards_east
				visited.append((towards_north + dist, towards_east))
			towards_north += int(dir[1])
		elif direction == 1:
			for dist in range(1,int(dir[1]) + 1):
				if (towards_north, towards_east + dist) in visited:
					return towards_north, towards_east + dist
				visited.append((towards_north, towards_east + dist))
			towards_east += int(dir[1])
		elif direction == 2:
			for dist in range(1,int(dir[1]) + 1):
				if (towards_north - dist, towards_east) in visited:
					return towards_north - dist, towards_east
				visited.append((towards_north - dist, towards_east))
			towards_north -= int(dir[1])
		else:
			for dist in range(1,int(dir[1]) + 1):
				if (towards_north, towards_east - dist) in visited:
					return towards_north, towards_east - dist
				visited.append((towards_north, towards_east - dist))
			towards_east -= int(dir[1])

inFile = open('input.txt','r')
dir_list = inFile.read().split(", ")
dir_tuples = [direction_split(str) for str in dir_list]
(north, east) = process_directions(dir_tuples)
print(abs(north) + abs(east))
input("Press Enter to continue...")