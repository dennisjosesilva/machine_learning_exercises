import json
import sys
from pprint import pprint 
from Perceptron import Perceptron

json_file = open("samples.json")
samples = json.load(json_file)

perceptron = Perceptron(samples)

classifier = perceptron.run()

while(True):
	print("Entre com o valor a ser classificado (use CTRL+C para sair): ")
	x = input()
	
	y = classifier.classify(x)
	print("classe calculada pelo perceptron: " + str(y))
