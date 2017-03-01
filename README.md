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


CSV FILE ITEMS:

| ID | TITLE | ARTIST NAME | RELEASE | YEAR | KEY | KEY CONFIDENCE | TIME SIGNATURE | TIME SIGNATURE CONFIDENCE | MODE | MODE CONFIDENCE | END OF FADE IN | START OF FADE OUT | ENERGY | DURATION |  DANCEABILITY | SONG HOTTNESS | TEMPO | LOUDNESS | 
| ------------- | ------------- | ------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |------------- |
| String              | String        | String                | String | Int | Float | | | | | | | | | | | | | |
| TRMMMYQ128F932D901  | Silent Night  | Monster Ballads X-Mas | 2003   | 10  | 0.777 | | | | | | | | | | | | | |
| TRMMMKD128F425225D  | Tanssi vaan   | Karkuteill\u00e4      | 1995   | 9   | 0.808 | | | | | | | | | | | | | |

{"mode_confidence": 0.688, "end_of_fade_in": 2.049, "key_confidence": 0.777, "energy": 0.0, "release_seven_digital_id": 633681, "year": 2003, "duration": 252.05506, "artist_mbid": "357ff05d-848a-44cf-b608-cb34b5701ae5", "track_seven_digital_id": "7032331", "time_signature_confidence": 0.94, "title": "Silent Night", "artist_playmeid": 44895, "track_id": "TRMMMYQ128F932D901", "artist_audio_md_five": "aee9820911781c734e7694c5432990ca", "danceability": 0.0, "song_hottnesss": 0.5428987432910862, "start_of_fade_out": 236.635, "tempo": 87.002, "artist_name": "Faster Pussy cat",  "song_id": "SOQMMHC12AB0180CB8", "mode": 0, "time_signature": 4, "loudness": -4.829}, 

{"mode_confidence": 0.355, "end_of_fade_in": 0.258, "key_confidence": 0.808, "energy": 0.0, "release_seven_digital_id": 145266, "duration": 156.55138, "artist_mbid": "8d7ef530-a6fd-4f8f-b2e2-74aec765e0f9", "track_seven_digital_id": "1514808", "time_signature_confidence": 0.0, "title": "Tanssi vaan", "artist_playmeid": -1, "track_id": "TRMMMKD128F425225D", "artist_audio_md_five": "ed222d07c83bac7689d52753610a513a", "danceability": 0.0, "song_hottnesss": 0.2998774882739778, "start_of_fade_out": 148.66, "tempo": 150.778, "artist_name": "Karkkiautomaatti", "song_id": "SOVFVAK12A8C1350D9", "mode": 1, "time_signature": 1, "loudness": -10.555},
