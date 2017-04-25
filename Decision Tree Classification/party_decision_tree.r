# Load the party package. It will automatically load other dependent packages.
library(party)

# Create the input data frame.
#input.dat <- read.csv(file="train_sample.csv",head=TRUE,sep=",")

traindata <- read.table(file="train_sample.csv", sep=",", header=TRUE)
testdata <- read.table(file="test_sample.csv", sep=",", header=TRUE)
#data <- read_data(df_train, df_test)

# Give the chart file a name.
png(file = "dt.png")

# Create the tree.
#year	+
model <- ctree(
  top100 ~  key	+ key_confidence
  +time_signature	+ time_signature_confidence	+ mode
  +mode_confidence+	end_of_fade_in	+ start_of_fade_out
  +energy+	duration+	danceability	+tempo+	loudness, 
  data = traindata)

pred <- predict(model, newdata = testdata) 

#get Confusion matrix
a = 0
b = 0
c = 0
d = 0
for(i in 1:length(pred)){
  if(pred[i]=='yes'){
    if(traindata[i,]$top100=='yes'){
      a = a + 1
    }
    else{
      c = c + 1
    }
  }
  else{
    if(traindata[i,]$top100=='no'){
      d = d + 1
    }
    else{
      b = b + 1
    }
  }
}


#get precision
precision = a/(a+c)

#get recall
recall = a/(a+b)

#get fmessure
fmessure = (2*a)/((2*a)+b+c)


plot(model)

# Save the file.
dev.off()

