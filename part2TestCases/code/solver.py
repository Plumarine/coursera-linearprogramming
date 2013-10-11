from dictionary import DictionaryFactory
from pivot import Pivotter

class LPSolver:

	def __init__(self):
		self.currDict = None
		self.steps	  = 0

	def solve(self):
		cDict = self.currDict
		final = cDict.isFinal()
		pivotter = Pivotter()
		while not final:
			nDict = pivotter.nextDictionary(cDict)
			print str(self.steps) + " : " + str(nDict.objectiveValue())
			self.steps += 1
			final = nDict.isFinal()
			cDict = nDict
		self.currDict = cDict

	def printDictionary(self):
		print self.currDict

	def readDictFromFile(self, filename):
		inputFile = open(filename, 'r')
		self.currDict = DictionaryFactory().createDictionary(inputFile)

	def printResult(self):
		if(self.currDict.isUnbounded()):
			print ("UNBOUNDED")
		else:
			print (str(self.currDict.objectiveValue()))
			print (str(self.steps))
			
	def writeResultIntoFile(self, filename):
		outputFile = open(filename, 'w')
		if(self.currDict.isUnbounded()):
			outputFile.write("UNBOUNDED")
		else:
			outputFile.write(str(self.currDict.objectiveValue()))
			outputFile.write("\n")
			outputFile.write(str(self.steps))
