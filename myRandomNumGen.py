#!/usr/local/bin/python3
import sys
import random

def createAndOpenTheFile(name):
	try:
		file = open(name, 'r+')
		return file
	except IOError:
		file = open(name, 'w+')
		return file

def generate(theList, seed, max):
	random.seed(seed, 2)
	i = 0
	while (i < 10):
		rand = random.randint(0, max)
		theList.append(rand)
		i += 1

def writeInFile(theFile, theList):
	for x in theList:
		theFile.write(str(x))
		theFile.write(';')
	theFile.write('\n')

def main():
	theSeed = None
	listRand = []
	try:
		theFile = createAndOpenTheFile("randomGeneratedNumbers")
	except IOError:
		print("unable to create the file")
		exit()
	generate(listRand, theSeed, 100)
	print(listRand)
	writeInFile(theFile, listRand)
	theFile.close()
	#except:
	#	print("toto")
	#try:
	#	file = open('randomGeneratedNumbers', 'w+')
	#except:

main()
#for arg in sys.argv:
#	print (arg)