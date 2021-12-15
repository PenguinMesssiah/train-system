#class PLCInterpreter
#in Mike's folder

class PLCInterpreter(object):

	def __init__(self): #automatic is a boolean for auto vs maintenance mode
		self.filepath = ""
		self.automatic = True

	def runPLC(self, path, wayside):
		self.filepath = path
		with open(self.filepath, "r") as f:
			line = True
			while line:
				line = f.readline()
				print(line)

				#get block for results
				currBlock = line[:3].strip()
				try:
					currBlock = int(currBlock)
				except:
					break;
				print(currBlock)

				#result
				data = line[3]
				if data == 'a':
					print ('auth')
					wayside.authority_dict.update({currBlock: self.parseAuthority(line[5:], wayside)}) #should skip equal sign
					print(wayside.authority_dict)
				elif data == 'x':
					print('crossing')
					wayside.crossing_dict.update({currBlock: self.parseCrossing(line[5:], wayside)}) #should skip equal sign
					print(wayside.crossing_dict)
				elif data =='l':
					print('lights')
					#wayside.lights_dict.update({currBlock: self.parseLight(line[5:], wayside)})
					print(wayside.lights_dict)
				elif data == 'w':
					print('switch')
					wayside.switch_dict.update({currBlock: self.parseSwitch(line[5:], wayside)}) #should skip equal sign
					print(wayside.switch_dict)
				elif data == 'c':
					print('commanded speed')
					wayside.commanded_speed_dict.update({currBlock: self.parseCommandedSpeed(line[5:], wayside)}) #should skip equal sign
					print(wayside.commanded_speed_dict)

			f.close()
		#print(file)

	def parseAuthority(self, rule, wayside):
		cursor = 0
		result = 0
		logic = rule[4]
		#args = [] #add arg values to an array and then and them
		#or running calculation <- try this first
		while cursor < len(rule):
			argBlock = rule[cursor:cursor+3].strip()
			try:
				argBlock = int(argBlock)
			except:
				argBlock = argBlock #doesn't like when you don't have anything
			print(argBlock)

			cursor = cursor+3
			print(cursor)
			if cursor >= len(rule):
				break
			src = rule[cursor]
			print("src= " + src)
			if src == 'a':
				print ('auth')
				arg = wayside.authority_dict[argBlock]
				print(argBlock, ":", arg)
			elif src == 's':
				print('schedule')
				arg = wayside.authority_limit_dict[argBlock]
				print(argBlock, ":", arg)
			elif src =='o':
				print('occ')
				print(argBlock)
				arg = wayside.occupancyCTC_dict[argBlock]
				print(argBlock, ":", arg)
			elif src == 'w':
				print('switch')
				arg = wayside.switch_dict[argBlock]
				print(argBlock, ":", arg)

			cursor = cursor + 1
			if cursor >= len(rule):
				break

			#and or or
			if logic == '&':
				if cursor <=4:
					result = arg and arg
				else:
					result = result and arg
			elif logic == '|':
				if cursor <=4:
					result = arg or arg
				else:
					result = result or arg

			print("result= ", result)
			cursor = cursor + 1
		return result

	def parseCommandedSpeed(self, rule, wayside):
		cursor = 0
		result = 0
		logic = rule[4]
		#args = [] #add arg values to an array and then and them
		#or running calculation <- try this first
		while cursor < len(rule):
			argBlock = rule[cursor:cursor+3].strip()
			try:
				argBlock = int(argBlock)
			except:
				argBlock = argBlock #doesn't like when you don't have anything
			print(argBlock)

			cursor = cursor+3
			print(cursor)
			if cursor >= len(rule):
				break
			src = rule[cursor]
			print("src= " + src)
			if src == 'a':
				print ('auth')
				arg = wayside.authority_dict[argBlock]
				print(argBlock, ":", arg)
			elif src == 's':
				print('schedule')
				arg = wayside.authority_limit_dict[argBlock]
				print(argBlock, ":", arg)
			elif src =='o':
				print('occ')
				print(argBlock)
				arg = wayside.occupancyCTC_dict[argBlock]
				print(argBlock, ":", arg)
			elif src == 'w':
				print('switch')
				arg = wayside.switch_dict[argBlock]
				print(argBlock, ":", arg)

			cursor = cursor + 1
			if cursor >= len(rule):
				break

			#and or or
			if logic == '&':
				if cursor <=4:
					result = arg and arg
				else:
					result = result and arg
			elif logic == '|':
				if cursor <=4:
					result = arg or arg
				else:
					result = result or arg

			print("result= ", result)
			cursor = cursor + 1
		return result


	def parseCrossing(self, rule, wayside):
		cursor = 0
		result = 0
		logic = rule[4]
		#args = [] #add arg values to an array and then and them
		#or running calculation <- try this first
		while cursor < len(rule):
			argBlock = rule[cursor:cursor+3].strip()
			try:
				argBlock = int(argBlock)
			except:
				argBlock = argBlock #doesn't like when you don't have anything
			print(argBlock)

			cursor = cursor+3
			print(cursor)
			if cursor >= len(rule):
				break
			src = rule[cursor]
			print("src= " + src)
			if src == 'a':
				print ('auth')
				arg = wayside.authority_dict[argBlock]
				print(argBlock, ":", arg)
			elif src == 's':
				print('schedule')
				arg = wayside.authority_limit_dict[argBlock]
				print(argBlock, ":", arg)
			elif src =='o':
				print('occ')
				print(argBlock)
				arg = wayside.occupancyCTC_dict[argBlock]
				print(argBlock, ":", arg)
			elif src == 'w':
				print('switch')
				arg = wayside.switch_dict[argBlock]
				print(argBlock, ":", arg)

			cursor = cursor + 1
			if cursor >= len(rule):
				break

			arg = not arg
			if rule[cursor] == ('&' or '|'):
				logic = rule[cursor]
			print("logic= ", logic)
			#and or or
			if logic == '&':
				if cursor <=4:
					result = arg and arg
				else:
					result = result and arg
			elif logic == '|':
				if cursor <=4:
					result = arg or arg
				else:
					result = result or arg

			print("result= ", result)
			cursor = cursor + 1
		if result == True:
			return 1
		return 0

	def parseSwitch(self, rule, wayside):
		return 0

#	def parseLight(self, rule, wayside):
#		cursor = 0
#		result = 0
#		end = rule.find(',')
#		currRule = rule[:end]
#		remaining = rule[end+1:]
#		last = False;
#		#args = [] #add arg values to an array and then and them
#		#or running calculation <- try this first
#		while cursor < len(rule):
#
#			#currRule = rule[:end]
#			#remaining = rule[end+1:]
#			cursor2 = 0
#			while cursor2 < len(currRule):
#				logic = currRule[4]
#				argBlock = currRule[cursor2:cursor2+3].strip()
#				try:
#					argBlock = int(argBlock)
#				except:
#					argBlock = argBlock #doesn't like when you don't have anything
#				print("argBlock: ", argBlock)
#
#				cursor2 = cursor2+3
#				print("cursor2: ", cursor2)
#				if cursor2 >= len(currRule):
#					break
#				src = currRule[cursor2]
#				print("src= " + src)
#				if src == 'a':
#					print ('auth')
#					arg = wayside.authority_dict[argBlock]
#					print(argBlock, ":", arg)
#				elif src == 's':
#					print('schedule')
#					arg = wayside.authority_limit_dict[argBlock]
#					print(argBlock, ":", arg)
#				elif src =='o':
#					print('occ')
#					print(argBlock)
#					arg = wayside.occupancyCTC_dict[argBlock]
#					print(argBlock, ":", arg)
#				elif src == 'w':
#					print('switch')
#					arg = wayside.switch_dict[argBlock]
#					print(argBlock, ":", arg)
#
#				cursor2 = cursor2 + 1
#				if cursor2 >= len(currRule):
#					break

				#lights are actually based on occupancy 0 = occupied
#				arg = not arg

				#and or or
#				if logic == '&':
#					if cursor2 <=4:
#						result = arg and arg
#					else:
#						result = result and arg
#				elif logic == '|':
#					print("MADE IT HERE")
#					if cursor2 <=4:
#						result = arg or arg
#					else:
#						result = result or arg
#				print("result= ", result)
#				cursor2 = cursor2 + 1
#			if result == True:
#				print("cursor2: ",rule[cursor2-1])
#				if currRule[cursor2-1] == 'r':
#					return [1, 0, 0, 0]
#				elif currRule[cursor2-1] == 'y':
#					return [0, 1, 0, 0]
#				elif currRule[cursor2-1] == 'g':
#					return [0, 0, 1, 0]
#				elif currRule[cursor2-1] == 's':
#					return [0, 0, 0, 1]
#			print("remaining: ", remaining)
#			start = end+1
#			print("start: ", start)
#			end = remaining.find(',')
#			if (end > -1):
#				print("end: ", end)
#				currRule = remaining[:end]
#				print("currRule: ", currRule)
#				remaining = remaining[end+1:]
#				cursor = cursor+start
#				print("cursor: ", cursor)
#			elif last == False:
#				currRule = remaining
#				last = True
#			else:
#				break;
#		return [0, 0, 0, 0]
