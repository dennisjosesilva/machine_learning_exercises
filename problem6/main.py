import json
import sys, getopt
from pprint import pprint 
from Perceptron import PerceptronGenerator


def main(argv):
	training_data_file = "samples.json"
	
	try:
		opts, args = getopt.getopt(argv, "ht:", ["tranning_data_file="])
	except getopt.GetoptError:
		print("Sintax: ")
		print("samples_generator.py -t <tranning_data_file>")
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == "h":
			print("Sintax: ")
			print("samples_generator.py -t <tranning_data_file>")
		elif opt in ("-t", "--tranning_data_file"):
			training_data_file = arg
	
	json_file = open(training_data_file)
	samples = json.load(json_file)

	perceptron = PerceptronGenerator()
	classifier = perceptron.generate(samples)

	while(True):
		print("Entre com o valor a ser classificado (use CTRL+C para sair): ")
		x = input()
		
		y = classifier.classify(float(x))
		print("classe calculada pelo perceptron: " + str(y))

if __name__ == '__main__':
	main(sys.argv[1:])
