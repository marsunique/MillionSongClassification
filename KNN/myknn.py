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
 
# 1) given two data points, calculate the euclidean distance between them
def calculate_Distance(data1, data2):
    points = zip(data1, data2)
    diffs_squared_distance = [pow(a - b, 2) for (a, b) in points]
    return math.sqrt(sum(diffs_squared_distance))
 
# 2) given a training set and a test instance, use getDistance to calculate all pairwise distances
def calculate_neighbours(training_set, test_instance, k):
    distances = [_get_tuple_distance(training_instance, test_instance) for training_instance in training_set]
    # index 1 is the calculated distance between training_instance and test_instance
    sorted_distances = sorted(distances, key=itemgetter(1))
    # extract only training instances
    sorted_training_instances = [tuple[0] for tuple in sorted_distances]
    # select first k elements
    return sorted_training_instances[:k]
 
def _get_tuple_distance(training_instance, test_instance):
    data1 = training_instance[0]
    data2 = test_instance

    points = zip(data1, data2)
    diffs_squared_distance = [pow(a - b, 2) for (a, b) in points]
    sum_result = math.sqrt(sum(diffs_squared_distance))
    return (training_instance, sum_result)
    #return (training_instance, calculate_Distance(test_instance, training_instance[0]))
 
# 3) given an array of nearest neighbours for a test case, tally up their classes to vote on test case class
def get_majority_vote(neighbours):
    # index 1 is the class
    classes = [neighbour[1] for neighbour in neighbours]
    count = Counter(classes)
    return count.most_common()[0][0] 
 
# setting up main executable method
def main():

    trian_data = load_data("train_sample.csv")
    test_data = load_data("test_sample.csv")
    train_label = load_label("train_sample_label.csv")
    test_label = load_label("test_sample_label.csv")
    # reformat train/test datasets for convenience
    train = np.array(zip(trian_data,train_label))
    test = np.array(zip(test_data, test_label))

    print("Finish loading data")
 
    # generate predictions
    predictions = []
 
    # let's arbitrarily set k equal to 5, meaning that to predict the class of new instances,
    k = 5
 
    # for each instance in the test set, get nearest neighbours and majority vote on predicted class
    for x in range(len(test_data)):
 
            print 'Classifying test instance number ' + str(x) + ":",
            neighbours = calculate_neighbours(training_set=train, test_instance=test[x][0], k=5)
            majority_vote = get_majority_vote(neighbours)
            predictions.append(majority_vote)
            print 'Predicted label=' + str(majority_vote) + ', Actual label=' + str(test[x][1])
 
    # summarize performance of the classification
    print '\nThe overall accuracy of the model is: ' + str(accuracy_score(test_label, predictions)) + "\n"
    report = classification_report(test_label, predictions, target_names = iris.target_names)
    print 'A detailed classification report: \n\n' + report
 
if __name__ == "__main__":
    main()