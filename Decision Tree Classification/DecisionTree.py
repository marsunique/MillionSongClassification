import pandas as pd
from sklearn import tree

header = pd.read_csv('tenksongs(labeled).csv', nrows = 1).columns
print header
data = pd.read_csv('tenksongs(labeled).csv', skiprows = 0, header = None)
print data[1][1]

'''train_sample = []
train_labels = []
test_sample = []
yes_sample = []
train_count = 0
for i in range (0, len(data)):
	train_ele = []
	test_ele = []
	yes_ele = []
	if data[13][i] == 'yes':
		for j in range(0, 13):
			yes_ele.append(data[j][i])
		yes_sample.append(yes_ele)
		continue
	train_count = train_count + 1
	if train_count > 10000:
		continue
	for j in range(0, 13):
		train_ele.append(data[j][i])
	train_sample.append(train_ele)
	train_labels.append(data[13][i])
for i in range (0, 20):
	train_sample.append(yes_sample[i])
	train_labels.append('yes')
for i in range (20, 25):
	test_sample.append(yes_sample[i])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_sample, train_labels)
print clf.predict(test_sample)'''

'''X = [[0, 0], [1, 1]]
Y = ['yes', 'no']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print clf.predict([[0, 0.3]])'''
