import csv
import functools 
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('/vagrant/data-science-from-scratch/code/')
import working_with_data as wwd

def predict(beta0, beta1, x_i):
    return beta1 * x_i + beta0

def error(beta0, beta1, x_i, y_i):
    return y_i - predict(beta0, beta1, x_i)

def sum_of_squared_errors(beta0, beta1, x, y):
    return sum(error(beta0, beta1, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))

def make_cost_function(x, y):
	"""Returns sum_of_squared_errors as a function of betas, x and y are fixed."""
	return functools.partial(sum_of_squared_errors, x=x, y=y)

def load_ad_data():
	with open('Advertising.csv') as f:
		reader = csv.DictReader(f)
		data = [row for row in reader]

		parsers = {'Row': int, 'TV': float, 'Radio': float, 'Newspaper': float, 'Sales': float}
		data = [wwd.parse_dict(row, parsers) for row in data]
	return data

def make_contour_plot(J):
	beta0 = np.linspace(5, 10, num=100)
	beta1 = np.linspace(0.00, 0.10, num=90)
	js = [J(b0, b1) for b0 in beta0 for b1 in beta1]   # J(beta0, beta1) for every beta0,beta1 pair
	js = np.reshape(js, (len(beta0),len(beta1)))
	js = js.transpose()
	plt.contour(beta0, beta1, js, 50)
	plt.xlabel('beta0')
	plt.ylabel('beta1')
	plt.title('J(beta0, beta1)')

def gradient_on_data(beta, x, y):
	beta0, beta1 = beta
	partial_deriv0 = -sum(2*(y_i - predict(beta0, beta1, x_i))
		for x_i, y_i in zip(x, y))
	partial_deriv1 = -sum(2*(y_i - predict(beta0, beta1, x_i))*x_i
		for x_i, y_i in zip(x, y))
	return (partial_deriv0, partial_deriv1)

def make_gradient(x, y):
	return functools.partial(gradient_on_data, x=x, y=y)

