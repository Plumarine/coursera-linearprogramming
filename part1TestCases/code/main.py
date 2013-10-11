import os, sys
from dictionary import Dictionary, DictionaryFactory


if __name__ == "__main__":
	for filename in os.listdir(sys.argv[1]):
		if(filename[:4] == 'dict' and len(filename) < 7):
			inputFile = open(filename, 'r')
			dictionary = DictionaryFactory().createDictionary(inputFile)
			outputFile = open(filename + '.out', 'w')
			dictionary.writeResult(outputFile)
		if(filename.split('.')[-1] == 'dict'):
			inputFile = open(filename, 'r')
			dictionary = DictionaryFactory().createDictionary(inputFile)
			outputFile = open(filename + '.out', 'w')
			dictionary.writeResult(outputFile)