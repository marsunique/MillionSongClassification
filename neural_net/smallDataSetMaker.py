import re

totalCount = 0
successfulCount = 0
with open("millionSongs(labeled).csv", "r+") as inFile:
    
    for line in inFile:
        totalCount = totalCount + 1
        splitLine = line.split(",")
        if totalCount % 1000 == 0:
            print splitLine[len(splitLine)-1]
        
        if "yes" in splitLine[len(splitLine)-1]:
            successfulCount = successfulCount + 1


print "total:      " + str(totalCount)
print "successful: " + str(successfulCount)
