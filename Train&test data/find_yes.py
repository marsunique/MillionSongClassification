import csv
import pandas as pd

header = pd.read_csv('millionSongs(labeled).csv', nrows = 1).columns
totalData = pd.read_csv('millionSongs(labeled).csv', skiprows = 0, header = None)
colNum = len(header)
dataNum = len(totalData)


yes_data = []
print ">>> Extracting data",
extractCounter = 0
for j in range (0, dataNum) :
	extractCounter += 1
	if extractCounter == 10000:
		print ".",
		extractCounter = 0
	yesEle = []
	if totalData[colNum-1][j] == 'yes' :
		for i in range(0, colNum):
			yesEle.append(totalData[i][j])
		yes_data.append(yesEle)


print " "
print ">>> Now start saving data"




print ">>> Writing train data into yes_sample.csv",
with open('yes_sample.csv', 'w') as csvfile:
    saveCount = 0
    fieldnames = header
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    for yes_ele in yes_data:
        saveCount += 1
        if saveCount == 10000:
            print ".",
            saveCount = 0
    	rowDict = {}
    	for i in range(0, colNum):
    		rowDict[fieldnames[i]] = yes_ele[i]
    	writer.writerow(rowDict)
    csvfile.close()