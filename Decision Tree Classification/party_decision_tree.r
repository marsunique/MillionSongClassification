# Load the party package. It will automatically load other dependent packages.
library(party)
library("partykit")


# Create the input data frame.
#input.dat <- read.csv(file="train_sample.csv",head=TRUE,sep=",")

df_train <- read.table(file="train_sample.csv", sep=",", header=TRUE)
#df_test <- read.table(file="test_sample.csv", sep=",", header=TRUE)
#data <- read_data(df_train, df_test)

# Give the chart file a name.
png(file = "dt.png")

# Create the tree.
output.tree <- ctree(
  top100 ~ year	+ key	+ key_confidence
  +time_signature	+ time_signature_confidence	+ mode
  +mode_confidence+	end_of_fade_in	+ start_of_fade_out
  +energy+	duration+	danceability	+tempo+	loudness, 
  data = df_train)

plot(output.tree, tp_args = list(text = "vertical", ymax = 30))
# Plot the tree.
#rpart.plot(output.tree)

# Save the file.
dev.off()
