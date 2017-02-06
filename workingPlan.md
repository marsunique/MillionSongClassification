# CSC_522

###PROJECT: ALGO-RHYTHM

###Team Name: Skinny White Godzillas, Thick Grunting Diggers, Unemployed Wheelers, Old Driver

##Overview
###Language(s) we are using 

We will be using Java and Python *and tensorflow and...??*

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

*At what level are we implementing these?  Both Python and Java have libraries that will do any of these for us.  Are we allowed to use those?  Are we implementing from scratch?*


####Preprocessing

We will most likely use Java to parse the .h5 files since it has a built-in functionality to parse the .h5 formats.  We will most likely remove the unstructured data, and export our results as JSON or .csv files.

* The easiest way to do any project is not mixing languages if you don't need to.  We can get away with it if we want because this isn't a real project. Because we will have to pass data between ourselves, we still need to make some formatting standards.  i.e. if we're going to share code it is a good idea to just pick one language.  If we are going to each do our own thing (or each group do its own thing) then we need to agree that the preprocessor always outputs .csv files (or something) in a certain format, and the miners always output .csv files (or something) with a specific format.  That also means we have to agree on what the output of the clusterers/classifiers/etc will be (predicted-actual?).  Otherwise doing postprocessing/visualization will be a nightmare because the results from each group won't have the same information.

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

####Outlier Detectors (if any)

--PCA-- PCA isn't usually used to detect outliers.  We could probably only do one of the following types if we want.

- Statistical
- Density
- Clustering

####Postprocessing

Use data visualization techniques to display the result more interactively



###Division of Labor

First step: Are we breaking it up by task, by level?  Is one person/group writing each of these? Are some people focusing entirely on preprocessing and/or postprocessing, or are those going to be a group effort?


### Did It Work?
Somewhere, we need to say how we are measuring if it works.  Purely if we are right/wrong?  Number of false positives/false negatives?  For clustering, number of things in the wrong cluster, or are some songs more important than others?
