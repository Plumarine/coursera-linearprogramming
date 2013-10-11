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
			readOrder = [ self.__readNumberOfVariables,
                self.__readBasic, self.__readNoBasic,
                self.__readVectorB, self.__readMatrixA,
				self.__readObjective ]
			for i in range(len(readOrder)):
				readOrder[i](inputFile)
			self.basic = set(self.basic)
			self.noBasic = set(self.noBasic)
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
		self.consts = dict(zip(self.basic, vector))

	def __readMatrixA(self, inputFile):
		self.coefs = dict()
		for k in self.basic:
			line = inputFile.next()
			self.coefs[k] = dict(zip(self.noBasic, lineAsFloat(line)))

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
		instance.consts = self.consts
		instance.coefs = self.coefs
		instance.objective = self.objective
		return instance

class Dictionary:

	def __init__(self):
		self.unbounded = False
		self.basic = set()
		self.noBasic = set()
		self.objective = dict()
		self.consts = dict()
		self.coefs = dict()

	def objectiveValue(self):
		return self.objective[0]

	def isUnbounded(self):
		return self.unbounded

	def isDegenerated(self):
		return 0 in self.consts.values()

	def enteringVariable(self):
		try:
			return min({k for k in self.noBasic if self.objective[k] > 0 })
		except ValueError:
			return None

	def leavingVariable(self, entering):
		minQuocient = float("Inf")
		leaving = set()
		for k in self.basic:
			bij = self.consts[k]
			aij = self.coefs[k][entering]
			if(aij >= 0):
				continue
			quocient = (- bij/aij)
			if(quocient >= 0 and minQuocient > quocient):
				minQuocient = quocient
				leaving.clear()
				leaving.add(k)
			elif(quocient >= 0 and minQuocient == quocient):
				leaving.add(k)
		if(not leaving):
			self.unbounded = True
			raise UnboundedProblemException
		return min(leaving)

	def isFinal(self):
		return self.isUnbounded() or (not self.enteringVariable())

	def __str__(self):
		try:
			strl =  "Basic Variables : " + str(self.basic) + "\n"
			strl += "Non Basic Variables : " + str(self.noBasic) + "\n"
			strl += "Constants Vector : " + str(self.consts) + "\n"
			strl += "Coeficients Matrix\n"
			for k in self.basic:
				strl += str(k) + " := "
				strl += str(self.coefs[k]) + "\n"
			strl += "Objective : " + str(self.objective)
		except KeyError:
			pass
		finally:
			return strl

