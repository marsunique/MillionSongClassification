import os

newOutArray = []
with open("train_sample_II.csv", "r+") as inFile:
    for line in inFile:
        splitUp = line.split(",")
        for j in range(0,len(splitUp)-1):
            if "nan" in splitUp[j]:
                splitUp[j] = "0"
        s = ","
        newOutArray.append(s.join(splitUp))


with open("train_sample_III.csv", "w+") as outFile:
    for line in newOutArray:
        outFile.write(line)
        #outFile.write("\n")
                
