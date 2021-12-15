#class PLCInterpreter
#Elissa Wilton

class PLCInterpreter(object):

	def __init__(self): #automatic is a boolean for auto vs maintenance mode
		self.filepath = ""
		self.automatic = True

	def newPLC(self, path, wayside):
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
					wayside.blockAuth.update({currBlock: self.parseRule(line[5:], wayside)}) #should skip equal sign
					print(wayside.blockAuth)
				elif data == 's':
					print('schedule')
				elif data =='o':
					print('occ')
				elif data == 'w':
					print('switch')

			f.close()
		#print(file)

	def parseRule(self, rule, wayside):
		cursor = 0
		result = 0
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
				arg = wayside.blockAuth[argBlock]
				print(argBlock, ":", arg)
			elif src == 's':
				print('schedule')
				arg = wayside.blockCTCAuth[argBlock]
				print(argBlock, ":", arg)
			elif src =='o':
				print('occ')
				print(argBlock)
				arg = wayside.blockOcc[argBlock]
				print(argBlock, ":", arg)
			elif src == 'w':
				print('switch')
				arg = wayside.switches[argBlock]
				print(argBlock, ":", arg)

			cursor = cursor + 1
			if cursor >= len(rule):
				break

			#and or or
			if rule[cursor] == '&':
				if cursor <=4:
					result = arg and arg
				else:
					result = result and arg
			elif rule[cursor] == '|':
				if cursor <=4:
					result = arg or arg
				else:
					result = result or arg

			print("result= ", result)
			cursor = cursor + 1
		return result



 