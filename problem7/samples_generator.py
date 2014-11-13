import sys, getopt
import json
import random

class BoundEnum:
	LOWER_BOUND = 1
	UPPER_BOUND = 2

def generate_samples(samples_number, bound, threshold, ini, end):
	samples = []
	for i in range(1, samples_number):
		xvalue = random.uniform(ini, end)
		yvalue = -1		
		if is_valued_1(threshold, xvalue, bound):
			yvalue = 1
		samples.append((xvalue, yvalue))

	return samples

def is_valued_1(threshold, value_test, bound):
	if bound == BoundEnum.LOWER_BOUND:
		if value_test <= threshold:
			return True
		return False
	else:
		if value_test >= threshold:
			return True
		return False
			

def save_json(samples, output_file):
	with open(output_file, "w") as output:
		json.dump(samples, output)



def main(argv):
	samples_number = 100
	threshold = 5.0
	ini = 0.0
	end = 10.0
	output_file = "samples.json" 
	bound = None
	
	try:
		opts, args = getopt.getopt(argv, "hb:s:t:i:e:o:", ["bound=", "samples-number=", "threshold=", "ini=", "end=", "output-file="])
	except getopt.GetoptError:
		print("Sintax: ")
		print("samples_generator.py -b <lower|upper> -s <sample_number> -t <threshold> -i <ini> -e <end> -o <output_file>")
		sys.exit(2)

	for opt, arg in opts:
		if opt == "h":
			print("Sintax: ")
			print("samples_generator.py -s <sample_number> -t <threshold> -i <ini> -e <end> -o <output_file>")
		elif opt in ("-s", "--samples-number"):
			sample_number = arg
		elif opt in ("-t", "--threshold"):
			threshold = float(arg)
		elif opt in ("-i", "--ini"):
			ini = arg
		elif opt in ("-e", "--end"):
			end = arg
		elif opt in ("-o", "--output-file"):
			output_file = arg
		elif opt in ("-b", "--bound"):
			if arg == "lower":
				bound = BoundEnum.LOWER_BOUND
			elif arg == "upper":
				bound = BoundEnum.UPPER_BOUND
	
	if bound is None:
		print("bound argument must be informed")
		sys.exit(2)
	
	samples = generate_samples(samples_number, bound, threshold, ini, end)
	save_json(samples, output_file)
	
if __name__ == '__main__':
	main(sys.argv[1:])
