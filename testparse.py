#!/usr/bin/env

# Promulgate Big parser in Python
# ---------------------------------
# By Erin RobotGrrl for RobotMissions.org
# April 4th, 2019

# test strings
#api_str = ",432!#L1,255,R1,255!"
#api_str = " #L1,255,R1,255!"
api_str = "#J1,0,Q2,0!\r\n"
#api_str = " #L1,255,R1,255!erwer"
#api_str = ",432!#L1,255,R,1,255!"

# api message
action_specifier = ''
command1 = ''
key1 = ''
value1 = ''
command2 = ''
key2 = ''
value2 = ''
delimeter = ''

# protocol info
valid_actions = ['$', '^', '#', '@']
valid_delimeters = ['!', '?', ';']

# global vars
clean_str = []
split_str = []
split_start_ind = -1
why_ind = -1


# step 1) quick first check
def first_check():
	first_check_pass = False
	action_specifier_found = False
	delimeter_found = False
	for a in valid_actions:
		if clean_str.find(a) > -1:
			action_specifier_found = True
			#print("contains action specifier")
	for d in valid_delimeters:
		if clean_str.find(d) > -1:
			delimeter_found = True
			#print("contains delimeter")
	if action_specifier_found and delimeter_found:
		first_check_pass = True
	return first_check_pass


# step 2) parse the string and find the starting indices
def parse_and_find_indices():
	# split the string where the commas are
	global split_str
	split_str = clean_str.split(',')
	#print(split_str)

	# check to make sure the split has the action specifier
	# if not, set the split_start_ind to where it is
	global split_start_ind
	split_start_ind = 0
	found1 = False
	for blip in split_str:
		for a in valid_actions:
			if blip.find(a) > -1:
				#print("blip = %s split_start_ind = %d" % (blip, split_start_ind))
				found1 = True
				break
		if found1 == True:
			break
		split_start_ind = split_start_ind+1

	# check the action specifier is at index 0
	# if not, set the start_ind to where it is
	# (sorry, the variable names don't make sense)
	action_split_str = split_str[split_start_ind]
	#print("action_split_str %s" % action_split_str)
	start_ind = 0
	global why_ind
	why_ind = 0
	found = False
	for a in valid_actions:
		why_ind = 0
		if start_ind >= len(action_split_str)-1:
			break
		c = action_split_str[start_ind]
		for c in action_split_str:
			if a == c:
				#print("a == %s , c == %s , start_ind = %d , why_ind = %d" % (a, c, start_ind, why_ind))
				found = True
				break
			why_ind = why_ind+1
		start_ind = start_ind+1
		if found == True:
			break

	#print("split_start_ind = %d" % (split_start_ind))

	return found1


# step 3) set the variables based on the indices
def set_the_variables():
	
	global action_specifier
	global command1
	global key1
	global value1
	global command2
	global key2
	global value2
	global delimeter

	set_failed = False
	try:
		action_specifier = split_str[split_start_ind+0][why_ind]
	except:
		#print("action_specifier")
		set_failed = True

	try:
		command1 = split_str[split_start_ind+0][why_ind+1]
	except:
		#print("command1")
		set_failed = True

	try:
		key1 = int(split_str[split_start_ind+0][why_ind+2])
	except:
		#print("key1")
		set_failed = True

	try:
		value1 = int(split_str[split_start_ind+1])
	except:
		#print("value1")
		set_failed = True

	try:
		command2 = split_str[split_start_ind+2][0]
	except:
		#print("command2")
		set_failed = True

	try:
		key2 = int(split_str[split_start_ind+2][1])
	except:
		#print("key2")
		set_failed = True

	for d in valid_delimeters:
		if d in split_str[split_start_ind+3]:
			try:
				value2 = int( split_str[split_start_ind+3].split(d)[0] )
			except:
				#print("value2")
				set_failed = True
			delimeter = d

	return set_failed


# step 4) print the packet
def print_packet():
	print("Parsing: %s" % api_str)
	print("Action Specifier: %c" % action_specifier)
	print("Command 1: %c" % command1)
	print("Key 1: %d" % key1)
	print("Value 1: %d" % value1)
	print("Command 2: %c" % command2)
	print("Key 2: %d" % key2)
	print("Value 2: %d" % value2)
	print("Delimeter: %s" % delimeter)


clean_str = api_str.strip(' ')

if first_check() == True: # step 1
	if parse_and_find_indices() == True: # step 2
		if set_the_variables() == False:
			print_packet()
		else:
			print("Error step 3 - Did not set the variables")
	else:
		print("Error step 2 - Did not parse and find indices")
else:
	print("Error step 1 - Did not find the action specifier and delimeter")




