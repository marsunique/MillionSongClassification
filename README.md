# CSC_522

PROJECT: ALGO-RHYTHM

Team Name: Skinny White Godzillas, Thick Grunting Diggers, Unemployed Wheelers, Old Driver

Overview
Language(s) we are using 
We will be using Java and Python
Data set we are using
* http://labrosa.ee.columbia.edu/millionsong/
* http://labrosa.ee.columbia.edu/millionsong/pages/field-list 
Goal
Our goal is to classify songs with the focus of predicting if a song will make it to the top 40

Question(s) to Answer
3 easy questions to validate our setup
- 	Can we parse the .h5 files?
- 	Can we pick out the parts that we think will help us out the most?
- 	Can we attach song success/genre to the already existing songs?

2-6 medium questions we know we can do
Build a classification model
Cluster the songs
-	Instructions for how to write a hit song
- 	Show the trends of popular music

2-3 stretch goals that we may not even finish, but would be awesome if we did
Calculate the genre of a song (Rock, Pop, Country, etc) based on data points
Predict the number of weeks a song will be on the top 40
Recommender system for a user (based on user’s favorite genres, artists)



Plan - What Will We Use To Answer Questions

Preprocessing
We will most likely use Java to parse the .h5 files since it has a built-in functionality to parse the .h5 formats.  We will most likely remove the unstructured data, and export our results as JSON or .csv files.

Clustering Algorithms (if any)
k-means

Classification Algorithms (if any)
Convolutional neural network with TensorFlow, other algorithms we learn in class

Outlier Detectors (if any)
Principal components analysis

Postprocessing
Use data visualization techniques to display the result more interactively



Division of Labor


## CURRENT CSV FILE ITEMS ##

| ID | TITLE | ARTIST NAME | RELEASE | YEAR | KEY | KEY CONFIDENCE | TIME SIGNATURE | TIME SIGNATURE CONFIDENCE | MODE | MODE CONFIDENCE | END OF FADE IN | START OF FADE OUT | ENERGY | DURATION |  DANCEABILITY | SONG HOTTNESS | TEMPO | LOUDNESS | 
| ------------- | ------------- | ------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |
| String              | String        | String           | String                | String | Int | Float | Int | Float | Int | Float | Float | Float | Float | Float | Float | Float | Float | Float | Float |
| TRMMMYQ128F932D901  | Silent Night  | Faster Pussy cat | Monster Ballads X-Mas | 2003   | 10  | 0.777 | 4 | 0.94 | 0 | 0.688 | 2.049 | 236.635 | 0.0 | 252.05506 | 0.0 | 0.5428987432910862| 87.002 | -4.829 |
| TRMMMKD128F425225D  | Tanssi vaan   | Karkkiautomaatti |  Karkuteill\u00e4     | 1995   | 9   | 0.808 | 1 | 0.0 | 1 | 0.355 | 0.258 | 148.66 | 0.0 | 156.55138 | 0.0 | 0.2998774882739778| 150.778 | -10.555|

# Things have been done:

Parsing h5 file.

Preliminary selection of attributes (could be refined in the future, maybe more attributes will be incorporated).

Fix encoding problem. Transferred all characters to utf-8 format to avoid unexpected errors.

Done producing workable data (in .csv file).

# Things under processing:

Normalize the data.

Building classifier based on appropriate algorithms.
- 	Linear Regression
- 	L1 Penalized Linear Regression
- 	K-Nearest Neighbors Regression
Compare the performance between different algorithms.

Loading the data into mySQL.

Creating a labeled data set.

# Things to be done:

Generate hottness label in trainning data by using additional database (Billboard?).
Predict hottness of a song.

Optional: 
- 	Sentiment analysis based lyrics. 
- 	Explore themes and meanings of songs and incorporate these features into the dataset.


## Progress Report ##
Andrew - Have implemented Naive Bayes classifier and two outlier detection methods: a Support Vector Machine and a Random Forest.  Currently looking for outliers and trying to interpret the results of the detection methods.  For NB, next step is to see if some variables are easier to predict, and once we have Top 40 dataset, seeing if NB will predict song success.

Dustin - Created the parser for the .h5 files.  Parsed a subset of 10,000 songs into JSON format to be read by Yuchen's filters.  Currently creating a master history list of songs that reached the top 40 charts to be used as a starting point for our labeled data set.  Upon completion, we will extract the song data from the SQL database of all the songs that Marc will create.

Marc - Uploading and formatting data into a mySQL database for easy use. Will use in conjunction with Dustin's list of top 40 history to classify new songs as top 40 or not.
