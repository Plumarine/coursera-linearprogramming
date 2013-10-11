from solver import LPSolver
from sys import argv

def performSolve(inputFile, outputFile):
	print inputFile
	solver = LPSolver()
	solver.readDictFromFile(inputFile)
	solver.solve()
	solver.writeResultIntoFile(outputFile)
	solver.printResult()

if __name__ == "__main__":
	print argv
	for inputFile in argv[1:]:
		outputFile = inputFile + ".out"
		performSolve(inputFile,  outputFile)

