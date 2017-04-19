from sklearn.datasets import load_iris
from sklearn import cross_validation
from sklearn.metrics import classification_report, accuracy_score
from operator import itemgetter
import numpy as np
import math
from collections import Counter
import pandas as pd
import numpy
from numpy import genfromtxt
from sklearn import preprocessing

zero_one_scaler = preprocessing.MinMaxScaler() # convert data to range (0,1)

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
 
def myKNN(trainSet, testIns, k):
    distances = [euclidean_distance(trainIns, testIns) for trainIns in trainSet]
    # index 1 is the calculated distance between trainIns and testIns
    sorted_distances = sorted(distances, key=itemgetter(1))
    # extract only training instances
    sorted_training_instances = [t[0] for t in sorted_distances]
    # select first k elements
    neighbours = sorted_training_instances[:k]
    #majority vote
    classes = [neighbour[1] for neighbour in neighbours]
    count = Counter(classes)
    return count.most_common()[0][0] 
 
def euclidean_distance(trainIns, testIns):
    data1 = trainIns[0]
    data2 = testIns
    two_points_zip = zip(data1, data2)
    difference_square = [pow(a - b, 2) for (a, b) in two_points_zip]
    sum_result = math.sqrt(sum(difference_square))
    return (trainIns, sum_result)
 
def main():

    trian_data = load_data("train_sample.csv")
    test_data = load_data("test_sample.csv")
    train_label = load_label("train_sample_label.csv")
    test_label = load_label("test_sample_label.csv")
    # reformat train/test datasets for convenience
    train = np.array(zip(trian_data,train_label))
    test = np.array(zip(test_data, test_label))

    print("Finish loading data")
 
    predictions = []
 
    k = 5
 
    for x in range(len(test_data)):
            print 'Classifying test instance number ' + str(x) + ":",
            res = myKNN(trainSet=train, testIns=test[x][0], k=5)
            predictions.append(res)
            print 'Predicted label=' + str(res) + ', Actual label=' + str(test[x][1])
 
    print '\nThe overall accuracy of the model is: ' + str(accuracy_score(test_label, predictions)) + "\n"
    report = classification_report(test_label, predictions, target_names = iris.target_names)
    print 'A detailed classification report: \n\n' + report
 
if __name__ == "__main__":
    main()