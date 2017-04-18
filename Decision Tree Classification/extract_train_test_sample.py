#Author: Guanxu Yu
#Date: 04/09/2017
#At NC State University
#Note: To change the number of date in train set and test set, just to set "trainRatio" to your desire.

import csv
import pandas as pd

trainRatio = 0.7  # range from 0 to 1, trainRatio = number of data in train set / total data number

header = pd.read_csv('millionSongs(labeled).csv', nrows = 1).columns
totalData = pd.read_csv('millionSongs(labeled).csv', skiprows = 0, header = None)
colNum = len(header)
dataNum = len(totalData)

yesLabelNum = len(totalData[totalData[colNum-1] == 'yes']) # total number of data with "yes" label
noLabelNum = dataNum - yesLabelNum # total number of data with "no" label


trainYesNum = trainRatio * yesLabelNum # This is the numer of data with "yes" label in train set
trainNoNum = trainRatio * noLabelNum # This is the number of data with "no" label in train set

train_sample = []
test_sample = []

trainNoCount = 0
trainYesCount = 0

print ">>> Extracting data",
extractCounter = 0
for j in range (0, dataNum) :
	extractCounter += 1
	if extractCounter == 10000:
		print ".",
		extractCounter = 0
	trainEle = []
	testEle = []
	if totalData[colNum-1][j] == 'no' :
		if trainNoCount <= trainNoNum :
			trainNoCount = trainNoCount + 1
			for i in range(0, colNum):
				trainEle.append(totalData[i][j])
			train_sample.append(trainEle)
		else :
			for i in range(0, colNum):
				testEle.append(totalData[i][j])
			test_sample.append(testEle)
	else:
		if trainYesCount <= trainYesNum :
			trainYesCount = trainYesCount + 1
			for i in range(0, colNum):
				trainEle.append(totalData[i][j])
			train_sample.append(trainEle)
		else :
			for i in range(0, colNum):
				testEle.append(totalData[i][j])
			test_sample.append(testEle)
print " "
print ">>> Now start saving data"

print ">>> Writing train data into train_sample.csv",
with open('train_sample.csv', 'w') as csvfile:
    saveCount = 0
    fieldnames = header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    for train_ele in train_sample:
        saveCount += 1
        if saveCount == 10000:
            print ".",
            saveCount = 0
    	rowDict = {}
    	for i in range(0, colNum):
    		rowDict[fieldnames[i]] = train_ele[i]
    	writer.writerow(rowDict)
    csvfile.close()
print " "
print ">>> train_sample.csv has saved"
print " "
print ">>> Writing test data into test_sample.csv",

with open('test_sample.csv', 'w') as csvfile:
    saveCount = 0
    fieldnames = header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for test_ele in test_sample:
        saveCount += 1
        if saveCount == 10000:
            print ".",
            saveCount = 0
    	rowDict = {}
    	for i in range(0, colNum):
    		rowDict[fieldnames[i]] = test_ele[i]
    	writer.writerow(rowDict)
    csvfile.close()
print " "
print ">>> test_sample.csv has saved"




