![1](https://cloud.githubusercontent.com/assets/8572563/25414393/4b218236-29ff-11e7-9af2-1598f9cd67b0.png)
## Million Song Classification
Team Members: Yuchen Sun, Dustin Lambright, Guanxu Yu, Andrew Hill, Fuxing Luan, Marc Quaintance

## Google Drive Link For Data
https://drive.google.com/drive/folders/0B0UQJ5SM5N6geUoyQ3RxOHF4UEk?usp=sharing

## Overview
Algo-Rhythm is a collection of algorithms aimed at classifying a song as a successful song (reached the Billboard top 100 chart) or not.  We collected data from the [`LABROSA Million song dataset`](https://labrosa.ee.columbia.edu/millionsong/) and combined the songs with a successful label based on a result of our gathering data from a histroy of the [`Billboard Top 100 Charts`](http://www.billboard.com/charts/hot-100).  Using this data, we created some algorithms from built-in libraries, and some algorithms built from scratch to classify any new songs as potentially successful or no.

* XXXXXXXXXXXXX [`Poster`](https://labrosa.ee.columbia.edu/millionsong/)
* XXXXXXXXXXXXX [`Report`](https://reddit.com)

## Algorithms Implemented:

### [`Naive Bayes (without library)`](https://github.ncsu.edu/ysun34/CSC522_MillionSongClassification/tree/master/naiveBayes)

### Naive bayes, Linear Regression with LASSO, SVM and Outlier Methods <- Can't find andrew's folder??????
XXXXXXXXXXXXXXXX For details, see [`the included readme`](https://github.com/dlambright/CSC_522/tree/master/naiveBayes)

### [`Decision Tree`](https://github.ncsu.edu/ysun34/CSC522_MillionSongClassification/tree/master/Decision%20Tree%20Classification)

### [`kNN in R`](https://github.ncsu.edu/ysun34/CSC522_MillionSongClassification/tree/master/kNN_R)

### [`kNN in Python`](https://github.ncsu.edu/ysun34/CSC522_MillionSongClassification/tree/master/KNN)

### [`Neural Network`](https://github.ncsu.edu/ysun34/CSC522_MillionSongClassification/tree/master/neural_net)

### Song data parsing & feature selection
XXXXXXXXXXXXXXXX For details, see [`the included readme`](https://github.com/dlambright/CSC_522/tree/master/Preprocessing)


## CURRENT CSV FILE ITEMS ##

| ID | TITLE | ARTIST NAME | RELEASE | YEAR | KEY | KEY CONFIDENCE | TIME SIGNATURE | TIME SIGNATURE CONFIDENCE | MODE | MODE CONFIDENCE | END OF FADE IN | START OF FADE OUT | ENERGY | DURATION |  DANCEABILITY | SONG HOTTNESS | TEMPO | LOUDNESS | TOP 100? | 
| ------------- | ------------- | ------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |
| String              | String        | String           | String                | String | Int | Float | Int | Float | Int | Float | Float | Float | Float | Float | Float | Float | Float | Float | Bool |
| TRMMMYQ128F932D901  | Silent Night  | Faster Pussy cat | Monster Ballads X-Mas | 2003   | 10  | 0.777 | 4 | 0.94 | 0 | 0.688 | 2.049 | 236.635 | 0.0 | 252.05506 | 0.0 | 0.5428987432910862| 87.002 | -4.829 | 0 |
| TRMMMKD128F425225D  | Tanssi vaan   | Karkkiautomaatti |  Karkuteill\u00e4     | 1995   | 9   | 0.808 | 1 | 0.0 | 1 | 0.355 | 0.258 | 148.66 | 0.0 | 156.55138 | 0.0 | 0.2998774882739778| 150.778 | -10.555| 0 |


