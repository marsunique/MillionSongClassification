import re


totalCount = 0
successfulCount = 0
unsuccessfulCount = 0

successfulOut = open("successful.csv", "w")
unsuccessfulOut = open("unsuccessful.csv", "w")

with open("millionSongs(labeled).csv", "r+") as inFile:
    
    for line in inFile:
        if successfulCount > 100 and unsuccessfulCount > 100:
            break
        totalCount = totalCount + 1
        splitLine = line.split(",")
        if totalCount % 1000 == 0:
            print splitLine[len(splitLine)-1]
        
        if "yes" in splitLine[len(splitLine)-1]:
            successfulCount = successfulCount + 1
            successfulOut.write(line)
        
        elif unsuccessfulCount < 101:
            unsuccessfulCount = unsuccessfulCount + 1
            unsuccessfulOut.write(line)



print "total:      " + str(totalCount)
print "successful: " + str(successfulCount)
