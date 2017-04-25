This file is the readme for Naive Bayes, Linear Regression (with LASSO), SVM, and outlier detection methods One-Class SVM and Isolation Forest.

# ALGO-RHYTHM, Million Song Classification

Team Member: Yuchen Sun, Dustin Lambright, Guanxu Yu, Andrew Hill, Fuxing Luan, Marc Quaintance

## Google Drive Link For Data:
https://drive.google.com/drive/folders/0B0UQJ5SM5N6geUoyQ3RxOHF4UEk?usp=sharing
in the <i>NB Reg Outlier Data</i> folder

## Instructions
### NB, Linear Regression (with LASSO), SVM and Outlier Methods (with library)
The data these models use are in millionSongs3.txt and millionSongsString.txt in the above folder.  It runs using Python 2.6.

It can be run using any command line or environment which works for Python 2.6, and requires the random, timeit,  math, and sklearn python packages to be installed.  All of these come standard or can be installed using pip or easy_install.

This is set up to run <b> either </b> SVM and Naive Bayes <b> or </b> LASSO.  See directions below if you wish to run Linear Regression/LASSO.

#### Linear Regression

Because regression predicts on continuous variables, it is necessary to use a different measure of what is a "hit" prediction (e.g. binning answers).
  To use this method:
  * Uncomment the lines which predict for LASSO under the comment "LASSO".  
  * Comment out the lines under the headings "Naive Bayes" and "Support Vector Machine"
  * Change the confusion matrix generation.  There are two almost identical pieces of code at the bottom of the classificationBig method.  Uncomment the one with "pred > 0.5" which has the comment "use this one for lasso"
  and comment out the other.
  
  To switch back, do these steps in reverse.
  
  <b> NOTE </b> - Outlier detection takes a VERY long time.  It is recommended that the technique is tested on a small subset of the data (you can pass "testing=True" as a parameter) and/or commented out once it has been verified so as not to cause all other tests to take forever.
  
  

NB - Ensure that these files are in the same folder as the python file.  This code was run in Cloud9 on Ubuntu virtual machines.  If run in OSX it may require different file naming conventions.
Code which should address this is commented out in the readInput method.

