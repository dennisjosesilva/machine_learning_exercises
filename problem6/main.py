import json
from pprint import pprint 
from Perceptron import Perceptron

json_file = open("samples.json")
samples = json.load(json_file)

perceptron = Perceptron(samples)
print(perceptron.run())
