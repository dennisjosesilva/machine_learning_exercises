import numpy as np

class Perceptron:	
	def __init__(self, training_data):
		self.training_data = self._init_training_data(training_data)

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

	def run(self):
		w = np.zeros(2)
		iteration_count = 0

		while self._calculate_error(self.training_data ,w) > 0.0:			
			iteration_count += 1
			p = self._pick_a_misclassified_point(self.training_data, w)
			factor = [p[1] * x for x in p[0]]
			
			w += factor

			print("factor = w = " + str(p) + "itr = " + str(iteration_count))
			#input()

		return iteration_count