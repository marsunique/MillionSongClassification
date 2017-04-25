# Load the party package. It will automatically load other dependent packages.
library(party)

# Create the input data frame.
#input.dat <- read.csv(file="train_sample.csv",head=TRUE,sep=",")


#for case1
traindata <- read.table(file="train_sample.csv", sep=",", header=TRUE)
testdata <- read.table(file="test_sample.csv", sep=",", header=TRUE)
#data <- read_data(df_train, df_test)

#for case2
yesdata1 = traindata[traindata[,"top100"]=='yes', ]
yesdata2 = testdata[testdata[,"top100"]=='yes', ]
yesdata = rbind(yesdata1,yesdata2)
yestraindata = yesdata[c(1:1500),]
yestestdata = yesdata[c(1501:nrow(yesdata)),]


#for case3
nodata = testdata[testdata[,"top100"]=='no', ]
notraindata = nodata[c(1:5500),]
notestdata = nodata[c(10001:11000),]
combinedtraindata = rbind(yestraindata,notraindata)
combinedtestdata = rbind(yestestdata,notestdata)


# Give the chart file a name.
png(file = "dt.png")

# Create the tree. (original ratio)
model <- ctree(
  top100 ~  year + key	+ key_confidence
  +time_signature	+ time_signature_confidence	+ mode
  +mode_confidence+	end_of_fade_in	+ start_of_fade_out
  +energy+	duration+	danceability	+tempo+	loudness, 
  data = traindata)

# Create the tree2.  (all yes data)
model2 <- ctree(
  top100 ~  year + key	+ key_confidence
  +time_signature	+ time_signature_confidence	+ mode
  +mode_confidence+	end_of_fade_in	+ start_of_fade_out
  +energy+	duration+	danceability	+tempo+	loudness, 
  data = yestraindata)

# Create the tree3.   (1:5 ratio)
model3 <- ctree(
  top100 ~  year + key	+ key_confidence
  +time_signature	+ time_signature_confidence	+ mode
  +mode_confidence+	end_of_fade_in	+ start_of_fade_out
  +energy+	duration+	danceability	+tempo+	loudness, 
  data = combinedtraindata)

#pred1
pred1 <- predict(model, newdata = testdata) 

#pred2
pred2 <- predict(model2, newdata = yestestdata) 

#pred3
pred3 <- predict(model3, newdata = combinedtestdata) 


#table
table(pred1)
table(pred2)
table(pred3)


#get Confusion matrix 1
a1 = 0
b1 = 0
c1 = 0
d1 = 0
for(i in 1:length(pred1)){
  if(pred1[i]=='yes'){
    if(traindata[i,]$top100=='yes'){
      a1 = a1 + 1
    }
    else{
      c1 = c1 + 1
    }
  }
  else{
    if(traindata[i,]$top100=='no'){
      d1 = d1 + 1
    }
    else{
      b1 = b1 + 1
    }
  }
}

#get Confusion matrix 2
a2 = 0
b2 = 0
c2 = 0
d2 = 0
for(i in 1:length(pred2)){
  if(pred2[i]=='yes'){
    if(yestraindata[i,]$top100=='yes'){
      a2 = a2 + 1
    }
    else{
      c2 = c2 + 1
    }
  }
  else{
    if(yestraindata[i,]$top100=='no'){
      d2 = d2 + 1
    }
    else{
      b2 = b2 + 1
    }
  }
}

#get Confusion matrix 3
a3 = 0
b3 = 0
c3 = 0
d3 = 0
for(i in 1:length(pred3)){
  if(pred3[i]=='yes'){
    if(combinedtraindata[i,]$top100=='yes'){
      a3 = a3 + 1
    }
    else{
      c3 = c3 + 1
    }
  }
  else{
    if(combinedtraindata[i,]$top100=='no'){
      d3 = d3 + 1
    }
    else{
      b3 = b3 + 1
    }
  }
}


#get precision
precision1 = a1/(a1+c1)
precision2 = a2/(a2+c2)
precision3 = a3/(a3+c3)

#get recall
recall1 = a1/(a1+b1)
recall2 = a2/(a2+b2)
recall3 = a3/(a3+b3)

#get fmessure
fmessure1 = (2*a1)/((2*a1)+b1+c1)
fmessure2 = (2*a2)/((2*a2)+b2+c2)
fmessure3 = (2*a3)/((2*a3)+b3+c3)


print(precision1)
print(recall1)
print(fmessure1)

print(precision2)
print(recall2)
print(fmessure2)

print(precision3)
print(recall3)
print(fmessure3)


plot(model)

plot(model2)

plot(model3)

# Save the file.
dev.off()

