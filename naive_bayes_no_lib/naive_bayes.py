import re

bigArray = []
energyArray = []

artistNameArray = {}
keyDictionary = {}
timeSignatureDictionary = {}
modeDictionary = {}
fadeInDictionary = {}
fadeOutDictionary = {}
energyDictionary = {}


with open("train_sample.csv", "r+") as openFile:
    count = 0
    for line in openFile:
        newLine = line.split(",")
        if count != 0:
            bigArray.append(newLine)
        count = count + 1
    print "big array has " + str(len(bigArray))

#print bigArray[1]
#print bigArray[1][5]
#print bigArray[1][19]



for item in bigArray[1:]:
    # FIND THE NUMBER OF TIMES AN ARTIST SHOWS UP
    if "yes" in item[19]:
        key = item[2]
        artistNameArray.setdefault(key, 0)
        artistNameArray[key] = artistNameArray[key] + 1
    
    # KEY
    if float(item[6]) > .2:
        key = item[5]
        keyDictionary.setdefault(key, 0)
        keyDictionary[key] = keyDictionary[key] + 1
    else:
        key = 'unknown'
        keyDictionary.setdefault(key, 0)
        keyDictionary[key] = keyDictionary[key] + 1

    # TIME SIGNATURE
    if float(item[8]) > .25:
        key = item[7]
        timeSignatureDictionary.setdefault(key, 0)
        timeSignatureDictionary[key] = timeSignatureDictionary[key] + 1
    else:
        key = 'unknown'
        timeSignatureDictionary.setdefault(key, 0)
        timeSignatureDictionary[key] = timeSignatureDictionary[key] + 1

    # MODE
    if float(item[10]) > .25:
        key = item[9]
        modeDictionary.setdefault(key, 0)
        modeDictionary[key] = modeDictionary[key] + 1
    else:
        key = 'unknown'
        modeDictionary.setdefault(key, 0)
        modeDictionary[key] = modeDictionary[key] + 1

    #END OF FADE IN
    if float(item[11]) > 60:
        key = '60+'
        fadeInDictionary.setdefault(key, 0)
        fadeInDictionary[key] = fadeInDictionary[key] + 1
    elif float(item[11]) > 10:
        key = '10-60'
        fadeInDictionary.setdefault(key, 0)
        fadeInDictionary[key] = fadeInDictionary[key] + 1
    elif float(item[11]) > 5:
        key = '5-10'
        fadeInDictionary.setdefault(key, 0)
        fadeInDictionary[key] = fadeInDictionary[key] + 1
    elif float(item[11]) > 1:
        key = '1-5'
        fadeInDictionary.setdefault(key, 0)
        fadeInDictionary[key] = fadeInDictionary[key] + 1
    else:
        key = '1-'
        fadeInDictionary.setdefault(key, 0)
        fadeInDictionary[key] = fadeInDictionary[key] + 1

    #FADE OUT TIME
    fadeOut = float(item[14]) - float(item[12])
    if fadeOut > 60:
        key = '60+'
        fadeOutDictionary.setdefault(key, 0)
        fadeOutDictionary[key] = fadeOutDictionary[key] + 1
    elif fadeOut > 10:
        key = '10-60'
        fadeOutDictionary.setdefault(key, 0)
        fadeOutDictionary[key] = fadeOutDictionary[key] + 1
    elif fadeOut > 1:
        key = '1-10'
        fadeOutDictionary.setdefault(key, 0)
        fadeOutDictionary[key] = fadeOutDictionary[key] + 1
    else:
        key = '1-'
        fadeOutDictionary.setdefault(key, 0)
        fadeOutDictionary[key] = fadeOutDictionary[key] + 1

    #ENERGY
    energy = float(item[13])
    energyArray.append(energy)
    if energy > .75:
        key = '.75-1.00'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1
    elif energy > .50:
        key = '.50-.75'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1
    elif energy > .25:
        key = '.25-.50'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1
    elif energy > .01:
        key = '0.0-0.01'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1
    else:
        key = '0.0-.01'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1

    #ENERGY
    energy = float(item[13])
    energyArray.append(energy)
    if energy > .75:
        key = '.75-1.00'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1
elif energy > .50:
    key = '.50-.75'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1
    elif energy > .25:
        key = '.25-.50'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1
elif energy > .01:
    key = '0.0-0.01'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1
    else:
        key = '0.0-.01'
        energyDictionary.setdefault(key, 0)
        energyDictionary[key] = energyDictionary[key] + 1


'''
print len(artistNameArray)
for key in artistNameArray.keys():
    print key + "   " + str(artistNameArray[key])

# KEY
for key in keyDictionary:
    print key + "    " + str(keyDictionary[key])

# TIME SIGNATURE
for key in timeSignatureDictionary:
    print key + "    " + str(timeSignatureDictionary[key])

# MODE
for key in modeDictionary:
    print key + "    " + str(modeDictionary[key])


# START OF FADE OUT
for key in fadeInDictionary:
    print key + "    " + str(fadeInDictionary[key])

# START OF FADE OUT
for key in fadeOutDictionary:
    print key + "    " + str(fadeOutDictionary[key])
'''
# START OF FADE OUT
for key in energyDictionary:
    print key + "    " + str(energyDictionary[key])


#for item in energyArray:
#    print item

#print "fia" + str(max(fadeInArray))











