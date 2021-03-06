from __future__ import absolute_import
from __future__ import division
#from __future__ import print_function

import tensorflow as tf
import numpy as np

# Data sets
training_target = []
test_target = []
TRAINING = "train.csv"
TESTING = "millionSongsAltered.csv"


trainingData = []
'''
with open("train.csv") as inFile:
    for line in inFile:
        splitLine = line.split(",")
        training_target.append(int(splitLine[15]))
        splitLineSplit = splitLine[:-1]
        trainingData.append(splitLineSplit)

#print training_target
#training_set = np.asarray(trainingData, dtype=np.float64)
#training_set.target = training_target

testData = []
with open("train.csv") as inFile:
    for line in inFile:
        splitLine = line.split(",")
        testData.append(splitLine)

test_set = np.asarray(testData, dtype=np.float64)
'''
training_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=TRAINING,
    target_dtype=np.int,
                                                      features_dtype=np.float32)
#                                                      target_column=-1)


# Load datasets.
training_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=TRAINING,
                                                                   target_dtype=np.int,
                                                                   features_dtype=np.float32,
                                                                   target_column=-1)
print training_set.target
'''
test_set     = tf.contrib.learn.datasets.base.load_csv_with_header(filename=TESTING,
                                                                   target_dtype=np.int,
                                                                   features_dtype=np.float32,
                                                                   target_column=-1)
'''
'''
# Specify that all features have real-value data
feature_columns = [tf.contrib.layers.real_valued_column("", dimension = 18)]

# Build 3 layer DNN with 10, 20, 10 units respectively.
classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[10, 20, 10],
                                            n_classes=2,
                                            model_dir="/tmp/songs")

# Fit model.
classifier.fit(x=training_set.data,
               y=training_set.target,
               steps=2000)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(x=test_set.data,
                                     y=test_set.target)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))

# Classify two new flower samples.
new_samples = np.array(
                       [[6.4, 3.2, 4.5, 1.5], [5.8, 3.1, 5.0, 1.7]], dtype=float)
y = classifier.predict(new_samples)
print('Predictions: {}'.format(str(y)))


#track_id,title,artist_name,release,year,key,key_confidence,time_signature,ti    me_signature_confidence,mode,mode_confidence,end_of_fade_in,start_of_fade_ou    t,energy,duration,danceability,song_hottnesss,tempo,loudness,top100

'''
