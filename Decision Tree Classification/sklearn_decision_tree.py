#Auther: Guanxu Yu
#At NC State University
from __future__ import print_function

import os
import subprocess

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz

def get_train_data():
    df = pd.read_csv("train_sample.csv", index_col=0)
    return df

df_train = get_train_data()
def get_test_data():
	df = pd.read_csv("test_sample.csv", index_col=0)
	return df

df_test = get_test_data()

def encode_target(df, target_column):
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)

dfTest2, targetTest = encode_target(df_test, "top100")
df_test_data = df_test[list(dfTest2.columns[:14])]
actualTestLabel = dfTest2["Target"]

df2, targets = encode_target(df_train, "top100")
features = list(df2.columns[:14])

y = df2["Target"]
X = df2[features]
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)

dt.fit(X, y)

prediction = dt.predict(df_test_data)

testNum = len(actualTestLabel)

countMatch = 0.0
countYes = 0.0
totalYes = 0.0

trueTestLabel = []
for i in range(0, testNum):
	if actualTestLabel[i] == 0:
		trueTestLabel.append(1)
	else:
		trueTestLabel.append(0)

for i in range(0, testNum):    
	if trueTestLabel[i] == 1:
		totalYes += 1
	if trueTestLabel[i] == prediction[i] :
		countMatch += 1
		if prediction[i] == 1:
			countYes += 1

print("* Total match = ", countMatch, sep="\n", end="\n\n")
print("* Total yes = ", totalYes, sep="\n", end="\n\n")
print("* Total count yes = ", countYes, sep="\n", end="\n\n")

print("* Total Accuracy = ", countMatch/testNum, sep="\n", end="\n\n")
print("* Yes Accuracy = ", countYes/totalYes, sep="\n", end="\n\n")




