def lineAsInt(line):
	return map(int, (list(line.split())))

def lineAsFloat(line):
	return map(float, (list(line.split())))

class UnboundedProblemException(Exception):
	pass


class DictionaryFactory:
	
	def createDictionary(self, inputFile):
		self.readinputFile(inputFile)
		return self.getNewInstance()

	def readinputFile(self, inputFile):
		try:
			readOrder = [ self.__readNumberOfVariables, self.__readBasic, 
				self.__readNoBasic, self.__readVectorB, self.__readMatrixA,
				self.__readObjective ]
			for i in range(len(readOrder)):
				readOrder[i](inputFile)
		finally:
			inputFile.close()

	def __readNumberOfVariables(self, inputFile):
		line = inputFile.next()
		self.m, self.n = line.split()
		self.n = int(self.n)
		self.m = int(self.m)

	def __readBasic(self, inputFile):
		line = inputFile.next()
		self.basic = lineAsInt(line)

	def __readNoBasic(self, inputFile):
		line = inputFile.next()
		self.noBasic = lineAsInt(line)

	def __readVectorB(self, inputFile):
		line = inputFile.next()
		vector = lineAsFloat(line)
		self.b = dict(zip(self.basic, vector))

	def __readMatrixA(self, inputFile):
		self.A = dict()
		for k in self.basic:
			line = inputFile.next()
			self.A[k] = dict(zip(self.noBasic, lineAsFloat(line)))

	def __readObjective(self, inputFile):
		line = inputFile.next()
		vector = lineAsFloat(line)
		self.objective = dict(zip(self.noBasic, vector[1:]))
		self.objective[0] = vector[0]

	def getNewInstance(self):
		instance = Dictionary()
		instance.n = self.n
		instance.m = self.m
		instance.basic = self.basic
		instance.noBasic = self.noBasic
		instance.b = self.b
		instance.A = self.A
		instance.objective = self.objective
		return instance

class Dictionary:

	def objectiveValue(self):
		return self.objective[0]

	def enteringVariable(self):
		return min([k for k in self.noBasic if self.objective[k] > 0 ])

	def leavingVariable(self, entering):
		minQuocient = float("Inf")
		leaving = list()
		for k in self.basic:
			bij = self.b[k]
			aij = self.A[k][entering]
			quocient = - bij/aij if(aij != 0) else 0
			if(quocient > 0 and minQuocient > quocient):
				minQuocient = quocient
				leaving = list()
				leaving.append(k)
			if(quocient > 0 and minQuocient == quocient):
				leaving.append(k)
		if(not leaving):
			raise UnboundedProblemException
		return min(leaving)

	def objectiveNextValue(self, entering, leaving):
		oldObj  = self.objectiveValue()
		bj 		= self.b[leaving]
		ci 		= self.objective[entering]
		aij 	= self.A[leaving][entering]
 		return oldObj + ci * (bj/ - aij)

 	def writeCurrentResult(self, outputFile):
		self.writeResult(outputFile)

 	def writeResult(self, outputFile):
 		try:	
			entering 		= self.enteringVariable()
			leaving  		= self.leavingVariable(entering)
			objectiveValue  = self.objectiveNextValue(entering, leaving)
			outputFile.write(str(entering) + "\n")
			outputFile.write(str(leaving) + "\n")
			outputFile.write(str(objectiveValue))
		except UnboundedProblemException:
			outputFile.write("UNBOUNDED")
		finally:
			outputFile.flush()
			outputFile.close()


	def __str__(self):
		strl =  "Basic Variables : " + str(self.basic) + "\n"
		strl += "Non Basic Variables : " + str(self.noBasic) + "\n"
		strl += "Vector B : " + str(self.b) + "\n" 
		strl += "Matrix A\n"
		for k in self.basic:
			strl += str(k) + " := "
			strl += str(self.A[k]) + "\n"
		strl += "Objective : " + str(self.objective) 
		return strl
 