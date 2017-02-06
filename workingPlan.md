# CSC_522

###PROJECT: ALGO-RHYTHM

###Team Name: Skinny White Godzillas, Thick Grunting Diggers, Unemployed Wheelers, Old Driver

##Overview
###Language(s) we are using 

We will be using Java and Python

###Data set we are using
* http://labrosa.ee.columbia.edu/millionsong/
* http://labrosa.ee.columbia.edu/millionsong/pages/field-list 

###Goal

Our goal is to classify songs with the focus of predicting if a song will make it to the top 40

###Question(s) to Answer

####3 easy questions to validate our setup

- 	Can we parse the .h5 files?
- 	Can we pick out the parts that we think will help us out the most?
- 	Can we attach song success/genre to the already existing songs?

####2-6 medium questions we know we can do

Build a classification model

Cluster the songs

-	Instructions for how to write a hit song
- 	Show the trends of popular music

####2-3 stretch goals that we may not even finish, but would be awesome if we did

- Calculate the genre of a song (Rock, Pop, Country, etc) based on data points
- Predict the number of weeks a song will be on the top 40
- Recommender system for a user (based on user’s favorite genres, artists)



###Plan - What Will We Use To Answer Questions

####Preprocessing

We will most likely use Java to parse the .h5 files since it has a built-in functionality to parse the .h5 formats.  We will most likely remove the unstructured data, and export our results as JSON or .csv files.

+ what do we do about data that is incomplete?
+ What do we do about data that is contradictory?
+ What are we doing to address noise in the data?
+ How are we deciding what attributes are relevant?
+ How much data is needed for our methods to work?  Will we have that much data?  What do we do if we don't have enough in some group?
+ Do we need to discretize/bin any data?
+ Are we mining the full data or using a reduction technique (apart from removing irrelevant attributes)?
+ What will we do with string tags/metadata?  
+ What is the format of data when enters preprocessing?
+ What is the format of data when exiting preprocessing?
+ Do we have any data types that require standardization of formats (e.g. dates)?
+ Are we normalizing data or leaving attributes on original scale?

####Clustering Algorithms (if any)

k-means
* I would suggest at least 2 clustering techniques, maybe more.  Each should also be from a different type.
So I would suggest the following
- k-means
- pick one or more of following:
  * GMM
  * DBSCAN
  * Hierarchical Method

####Classification Algorithms (if any)

* same as above.  We should use more than one technique.  Since these are much easier, I'd say at least 3 of the following:

- Convolutional neural network 
- Bayes
- SVM
- a decision tree
- with TensorFlow, other algorithms we learn in class

####Outlier Detectors (if any)

PCA isn't usually used to detect outliers.  We could probably only do one of these types if we wanted.

- Statistical
- Density
- Clustering

####Postprocessing

Use data visualization techniques to display the result more interactively



###Division of Labor
