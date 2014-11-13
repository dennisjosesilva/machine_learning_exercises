import numpy as np
from abc import ABCMeta, abstractmethod

class Classifier:
	__metaclass__ = ABCMeta
		
	@abstractmethod
	def classify(self, x):
		pass
	
	
class PerceptronClassifier(Classifier):
	def __init__(self, w_vector):
		self.w = w_vector
	
	def _calculate_y_from_dot_product_calculated(self, y_calculated):
		if y_calculated < 0:
			return 0
		else: 
			return 1
	
	def classify(self, x):
		x_append_1 = [1, x]
		y_calculated = np.dot(x_append_1, self.w)
		#print(y_calculated)
		return self._calculate_y_from_dot_product_calculated(y_calculated)
	

class PerceptronGenerator:	
	def _init_training_data(self, training_data):
		pla_training_data = []
		for item in training_data:
			xs = [1, item[0]]
			y = item[1]
			pla_training_data.append([xs, y]) 

		return pla_training_data

	def _calculate_y_from_dot_product_calculated(self, value):
		if value < 0:
			return 0
		return 1

	def _is_misclassified(self, test, actual_value):
		calculated_y = self._calculate_y_from_dot_product_calculated(test)
		actual_y = self._calculate_y_from_dot_product_calculated(actual_value)
		
		if calculated_y == actual_y:
			return False

		return True

	def _calculate_error(self, input_vec ,w):
		number_of_samples = len(input_vec)
		misclassified_points_count = 0

		for p in input_vec:
			calculated_y = np.dot(p[0], w)
			if self._is_misclassified(calculated_y, p[1]):
				misclassified_points_count += 1

		return float(misclassified_points_count) / number_of_samples

	def _pick_a_misclassified_point(self, input_vec, w):
		for p in input_vec:
			calculated_y = np.dot(p[0], w)
			if self._is_misclassified(calculated_y, p[1]):
				return p

		return None

	def generate(self, training_data):
		w = np.zeros(2)
		iteration_count = 0
		
		pla_training_data = self._init_training_data(training_data)
		
		while self._calculate_error(pla_training_data ,w) > 0.0:			
			iteration_count += 1
			p = self._pick_a_misclassified_point(pla_training_data, w)
			factor = [p[1] * x for x in p[0]]
			
			w += factor

			#print("factor = w = " + str(p) + "itr = " + str(iteration_count))
			#input()

		return PerceptronClassifier(w)
