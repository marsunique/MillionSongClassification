#Auther: Guanxu Yu
#At NC State University
from __future__ import print_function

import os
import subprocess

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import time

def get_train_data():
    df = pd.read_csv("train_sample.csv", index_col=0)
    df = df.drop("artist_name", 1)
    df = df.drop("title", 1)
    df = df.drop("release", 1)
    df = df.drop("song_hottnesss", 1)
    return df

df_train = get_train_data()

def get_test_data():
    df = pd.read_csv("test_sample.csv", index_col = 0)
    df = df.drop("artist_name", 1)
    df = df.drop("title", 1)
    df = df.drop("release", 1)
    df = df.drop("song_hottnesss", 1)
    return df
df_test = get_test_data()
def reformat(data, classLabel):
    data2 = data.copy()
    labelDigitalValue = {'yes' : 1, 'no' : 0}
    data2["Target"] = data2[classLabel].replace(labelDigitalValue)
    return data2

dfTest2 = reformat(df_test, "top100")
df_test_data = df_test[list(dfTest2.columns[:14])]
actualTestLabel = dfTest2["Target"]

df2 = reformat(df_train, "top100")
features = list(df2.columns[:14])

y = df2["Target"]
X = df2[features]

start = time.time()
dt = DecisionTreeClassifier(max_depth = 36)

dt.fit(X, y)

prediction = dt.predict(df_test_data)
end = time.time()

testNum = len(actualTestLabel)

countMatch = 0.0
countYes = 0.0
totalYes = 0.0

yes_yes = 0
yes_no = 0
no_yes = 0
no_no = 0

trueTestLabel = []
for i in range(0, testNum):
	if actualTestLabel[i] == 0:
		trueTestLabel.append(0)
	else:
		trueTestLabel.append(1)

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

print("Total match = ", countMatch)
print("Total yes = ", totalYes)
print("Total count yes = ", countYes)

print("Total Accuracy = ", countMatch/testNum)
print("Yes Accuracy = ", countYes/totalYes)


print("yes_yes is ", yes_yes)
print("yes_no is ", yes_no)
print("no_yes is ", no_yes)
print("no_no is ", no_no)
print(end - start)


