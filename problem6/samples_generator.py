import sys, getopt
import json
import random

def generate_samples(samples_number, threshold, ini, end):
	samples = []
	for i in range(1, samples_number):
		xvalue = random.uniform(ini, end)
		yvalue = -1
		if xvalue >= threshold:
			yvalue = 1
		samples.append((xvalue, yvalue))

	return samples

def save_json(samples, output_file):
	with open(output_file, "w") as output:
		json.dump(samples, output)



def main(argv):
	samples_number = 100
	threshold = 5.0
	ini = 0.0
	end = 10.0
	output_file = "samples.json" 

	try:
		opts, args = getopt.getopt(argv, "hs:t:i:e:o:", ["samples-number=", "threshold=", "ini=", "end=", "output-file="])
	except getopt.GetoptError:
		print("Sintax: ")
		print("samples_generator.py -s <sample_number> -t <threshold> -i <ini> -e <end> -o <output_file>")
		sys.exit(2)

	for opt, arg in opts:
		if opt == "h":
			print("Sintax: ")
			print("samples_generator.py -s <sample_number> -t <threshold> -i <ini> -e <end> -o <output_file>")
		elif opt in ("-s", "--samples-number"):
			sample_number = arg
		elif opt in ("-t", "--threshold"):
			threshold = arg
		elif opt in ("-i", "--ini"):
			ini = arg
		elif opt in ("-e", "--end"):
			end = arg
		elif opt in ("-o", "--output-file"):
			output_file = arg
		
	samples = generate_samples(samples_number, threshold, ini, end)
	save_json(samples, output_file)
	
if __name__ == '__main__':
	main(sys.argv[1:])