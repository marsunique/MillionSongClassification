from operator import itemgetter
import numpy as np
import math
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
    distance = []
    for train_data in trainSet:
        distance.append(euclidean_distance(train_data, testIns))
    sorted_distances = sorted(distance, key=itemgetter(1))
    sorted_train_data = []
    for t in sorted_distances:
        sorted_train_data.append(t[0])
    neighbours = sorted_train_data[:k]
    #majority vote
    classes = []
    for neighbour in neighbours:
        classes.append(neighbour[1])
    class_dic = {0:0,1:0}

    for c in classes:
        class_dic[c] = class_dic[c] + 1

    if class_dic[0] > class_dic[1]:
        return 0
    else:
        return 1
 
def euclidean_distance(trainIns, testIns):
    data1 = trainIns[0]
    data2 = testIns
    vectorLength = len(data1)

    difference_square = []
    for i in range(vectorLength):
        aMinusbSquare = pow(data1[i] - data2[i], 2)
        difference_square.append(aMinusbSquare)
    res = math.sqrt(sum(difference_square))
    return (trainIns, res)
 
def main():

    trian_data = load_data("train_sample.csv")
    test_data = load_data("test_sample.csv")
    train_label = load_label("train_sample_label.csv")
    test_label = load_label("test_sample_label.csv")
    # reformat train/test datasets for convenience
    train = np.array(zip(trian_data,train_label))
    test = np.array(zip(test_data, test_label))

    print("Finish loading data")
 
    prediction = []
 
    k = 5
    
    for x in range(len(test_data)):
            print 'Classifying test instance number ' + str(x) + ":",
            res = myKNN(train, test[x][0], 5)
            prediction.append(res)
            print 'Predicted label=' + str(res) + ', Actual label=' + str(test[x][1])


    trueTestLabel = test_label
    testNum = len(trueTestLabel)
    countMatch = 0.0
    countYes = 0.0
    totalYes = 0.0
    yes_yes = 0
    yes_no = 0
    no_yes = 0
    no_no = 0

    for i in range(0, testNum):    
        if trueTestLabel[i] == 1:
            totalYes += 1
        if trueTestLabel[i] == prediction[i] :
            countMatch += 1
            if prediction[i] == 1:
                countYes += 1
                yes_yes += 1
            else:
                no_no += 1
        else:
            if trueTestLabel[i] == 1:
                yes_no += 1
            else:
                no_yes += 1

    print("* Total match = ", countMatch)
    print("* Total yes = ", totalYes)
    print("* Total count yes = ", countYes)

    print("* Total Accuracy = ", countMatch/testNum)
    print("* Yes Accuracy = ", countYes/totalYes)

    print("yes_yes is ", yes_yes)
    print("yes_no is ", yes_no)
    print("no_yes is ", no_yes)
    print("no_no is ", no_no)


if __name__ == "__main__":
    main()