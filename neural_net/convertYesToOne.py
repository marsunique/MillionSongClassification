import re

totalCount = 0
successfulCount = 0
unsuccessfulCount = 0

successfulOut = open("millionSongsAltered.csv", "w")
totalCount = 0
with open("millionSongs_labeled.csv", "r+") as inFile:
    
    for line in inFile:
        
        totalCount = totalCount + 1
        line = line.replace(",,,,,,,,,,,", "")
        splitLine = line.split(",")
        #print line
        #print splitLine
        #print len(splitLine)
        #print splitLine[len(splitLine)-1] 
        if "yes" in splitLine[len(splitLine)-1]:
            splitLine[len(splitLine)-1] = '1'
        else:
            splitLine[len(splitLine)-1] = '0'
            #splitLine[15] = '0'
        comma = ","
        outLine = comma.join(splitLine)
        successfulOut.write(outLine + "\n")
        
        


print "total:      " + str(totalCount)
print "successful: " + str(successfulCount)

