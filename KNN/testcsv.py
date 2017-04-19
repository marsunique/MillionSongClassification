import numpy
from numpy import genfromtxt
from sklearn import preprocessing
import pandas as pd

zero_one_scaler = preprocessing.MinMaxScaler()

def load_label(fileName):
	label = pd.read_csv(fileName)
	convert_label = []
	for x in label["top100"]:
		if x == "no":
			convert_label.append(0)
		else:
			convert_label.append(1)
	convert_label = numpy.array(convert_label)
	return convert_label

def load_data(fileName):
	my_data = genfromtxt(fileName, delimiter=',')
	my_data = zero_one_scaler.fit_transform(my_data)
	return my_data



