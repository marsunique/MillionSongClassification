import csv
import pandas as pd

'''with open('eggs.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})'''

trainRatio = 0.7  # range from 0 to 1

header = pd.read_csv('tenksongs(labeled).csv', nrows = 1).columns
totalData = pd.read_csv('tenksongs(labeled).csv', skiprows = 0, header = None)
colNum = len(header)
dataNum = len(totalData)
yesLabelNum = len(totalData[totalData[colNum-1] == 'yes'])
noLabelNum = dataNum - yesLabelNum


trainYesNum = trainRatio * yesLabelNum
trainNoNum = trainRatio * noLabelNum

train_sample = []
train_labels = []
test_sample = []
yes_sample = []

trainNoCount = 0
trainYesCount = 0

for j in range (0, dataNum):
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

with open('train_sample.csv', 'w') as csvfile:
    fieldnames = header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    for train_ele in train_sample:
    	rowDict = {}
    	for i in range(0, colNum):
    		rowDict[fieldnames[i]] = train_ele[i]
    	writer.writerow(rowDict)
    csvfile.close()


with open('test_sample.csv', 'w') as csvfile:
    fieldnames = header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for test_ele in test_sample:
    	rowDict = {}
    	for i in range(0, colNum):
    		rowDict[fieldnames[i]] = test_ele[i]
    	writer.writerow(rowDict)
    csvfile.close()





