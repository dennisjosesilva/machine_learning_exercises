import json
import sys, getopt
from pprint import pprint 
from Perceptron import PerceptronGenerator, ClassifierMergerWithAllTruth


def main(argv):
	lower_training_data_file = "lower_samples.json"
	upper_training_data_file = "upper_samples.json"

	try:
		opts, args = getopt.getopt(argv, "hl:u:", ["lower_bound_tranning_data_file=", "upper_bound_tranning_data_file="])
	except getopt.GetoptError:
		print("Sintax: ")
		print("samples_generator.py -l <lower_tranning_data_file> -u <upper_bound_tranning_data_file>")
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == "h":
			print("Sintax: ")
			print("samples_generator.py -l <lower_tranning_data_file> -u <upper_training_data_file>")
		elif opt in ("-l", "--lower_bound_tranning_data_file"):
			lower_training_data_file = arg
		elif opt in ("-u", "--upper_training_data_file" ):
			upper_training_data_file = arg
	
	
	perceptron_generator = PerceptronGenerator()

	#LOWER BOUND
	json_file = open(lower_training_data_file)
	samples = json.load(json_file)
	lower_bound_classifier = perceptron_generator.generate(samples)

	#UPPER BOUND
	json_file = open(upper_training_data_file)
	samples = json.load(json_file)
	upper_bound_classifier = perceptron_generator.generate(samples)	

	classifier = ClassifierMergerWithAllTruth([lower_bound_classifier, upper_bound_classifier])

	while(True):
		print("Entre com o valor a ser classificado (use CTRL+C para sair): ")
		x = input()
		
		y = classifier.classify(float(x))
		print("classe calculada pelo perceptron: " + str(y))

if __name__ == '__main__':
	main(sys.argv[1:])
