#kNN Implementation using R function then my own implementation

# load required libraries
require(class) # for kNN classifier
require(caret) # for createDataPartition, train, predict

#load in data
data <- read.csv(file = "millionSongs(labeled)_noNaN.csv", head = TRUE, sep = ",")

#remove variables not suitable for kNN
data.numbers <- data[, -c(1, 2, 3, 4, 5, 8, 10, 14, 16)]

#normalize variables ignoring
data.numbers[, -ncol(data.numbers)] <- scale(data.numbers[, -ncol(data.numbers)])

#split into train and test, 60% and 40% respectively
trainIdx <- createDataPartition(data.numbers[, 1], p = 0.6, list = FALSE)
testIdx <- setdiff(row(data.numbers), trainIdx[, 1])

#get the entries corresponding to the indices just found
train <- data.numbers[trainIdx, -ncol(data.numbers)]
test <- data.numbers[testIdx, -ncol(data.numbers)]

#get the classifications for the training data
classes <- factor(data.numbers[trainIdx, ncol(data.numbers)], labels=c("n", "y"))

#use the kNN function to predict test data
knnPreds <- knn(train, test, classes, k = 4, prob = TRUE)

#compare results of kNN to actual values
table(knnPreds, factor(data.numbers[testIdx, ncol(data.numbers)], labels=c("n", "y")))

#manually calculate kNN
myknn <- function(train, test, classes, k) {
  predicted <- vector()
  
  #for each test entry
  for(i in 1:nrow(test)) {
    dists <- vector()
    
    #check each training entry
    for(j in 1:nrow(train)) {
      distance <- 0
      
      #use manhattan distance for calculations
      for(a in 1:ncol(train)) {
        distance <- distance + abs(test[i, a] - train[j, a])
      }
      
      dists <- append(dists, distance)
    }
    
    #sort the distances and tally up the 
    indecies <- order(dists)[1:k]
    predicted[i] <- sort(classes[indecies], decreasing = TRUE)[1]
  }
  
  return(factor(predicted, labels=c("n", "y")))
}

#use myknn to predict
myPredictions <- myknn(train, test, classes, k = 1)

# compare results of my kNN to actual values
table(myPredictions, factor(data.numbers[testIdx, ncol(data.numbers)], labels=c("n", "y")))
