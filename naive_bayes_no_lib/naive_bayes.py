import re


class NaiveBayes(object):
    def __init__(self):
        self.train_data_path = 'train_sample.csv'
        self.train_data_yes = []
        self.train_data_no = []
        # number of rows
        self.total_row = 0
        self.row_number_yes = 0
        self.row_number_no = 0
        # label probability
        self.prob_yes = 0
        self.prob_no = 0
        # attributes conditional probability
        # ARTIST NAME
        self.prob_artistName_yes = {}
        self.prob_artistName_no = {}
        # KEY
        self.prob_key_yes = {}
        self.prob_key_no = {}
        # TIME SIGNATURE
        self.prob_timeSignature_yes = {}
        self.prob_timeSignature_no = {}
        # MODE
        self.prob_mode_yes = {}
        self.prob_mode_no = {}
        # FADE IN
        self.prob_fadeIn_yes = {}
        self.prob_fadeIn_no = {}
        # FADE OUT
        self.prob_fadeOut_yes = {}
        self.prob_fadeOut_no = {}
        # ENERGY
        self.prob_energy_yes = {}
        self.prob_energy_no = {}
        # DURATION
        self.prob_duration_yes = {}
        self.prob_duration_no = {}
        # DANCEABILITY
        self.prob_danceability_yes = {}
        self.prob_danceability_no = {}
        # HOTNESS
        self.prob_hotness_yes = {}
        self.prob_hotness_no = {}
        # TEMPO
        self.prob_tempo_yes = {}
        self.prob_tempo_no = {}
        # LOUDNESS
        self.prob_loudness_yes = {}
        self.prob_loudness_no = {}

    def readData(self):
        with open(self.train_data_path, 'r+') as openFile:
            count = 0
            for line in openFile:
                line = line.strip().split(",")
                count += 1
                if "yes" in line[19]:
                    self.train_data_yes.append(line)
                else:
                    self.train_data_no.append(line)
        openFile.close()
        self.train_data_no = self.train_data_no[1:]
        self.row_number_yes = len(self.train_data_yes)
        self.row_number_no = len(self.train_data_no)
        self.total_row = self.row_number_yes + self.row_number_no
        self.prob_yes = float(self.row_number_yes) / float(self.total_row)
        self.prob_no = float(self.row_number_no) / float(self.total_row)
        print 'Total number of data:', self.total_row
        print 'Number of YES:', self.row_number_yes
        print 'Number of NO:', self.row_number_no
        print 'P(yes):', self.prob_yes
        print 'P(no);', self.prob_no


if __name__ == '__main__':
    nb_model = NaiveBayes()
    nb_model.readData()


'''

unsuccessfulArray = []
successfulArray = []

durationArray = []

artistNameArray = {}
keyDictionary = {}
timeSignatureDictionary = {}
modeDictionary = {}
fadeInDictionary = {}
fadeOutDictionary = {}
energyDictionary = {}
durationDictionary = {}

danceabilityDictionary = {}
hotnessDictionary = {}
tempoDictionary = {}
loudnessDictionary = {}
labelDictionary = {}


with open("train_sample.csv", "r+") as openFile:
    count = 0
    for line in openFile:
        newLine = line.split(",")
        if count != 0:
            if "yes" in newLine[19]:
                successfulArray.append(newLine)
            else:
                unsuccessfulArray.append(newLine)
        count = count + 1
#print "big array has " + str(len(bigArray))

#print bigArray[1]
#print bigArray[1][5]
#print bigArray[1][19]


for item in successfulArray:
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

    #DURATION
    duration = float(item[14])
    durationArray.append(duration)
    if duration > 480:
        key = '480+'
        durationDictionary.setdefault(key, 0)
        durationDictionary[key] = durationDictionary[key] + 1
    elif duration > 270:
        key = '270-480'
        durationDictionary.setdefault(key, 0)
        durationDictionary[key] = durationDictionary[key] + 1
    elif duration > 120:
        key = '120-270'
        durationDictionary.setdefault(key, 0)
        durationDictionary[key] = durationDictionary[key] + 1
    elif duration > 10:
        key = '10-120'
        durationDictionary.setdefault(key, 0)
        durationDictionary[key] = durationDictionary[key] + 1
    else:
        key = '10-'
        durationDictionary.setdefault(key, 0)
        durationDictionary[key] = durationDictionary[key] + 1



    #DANCEABILITY
    danceability = float(item[15])
    if danceability > .20:
        key = '.20-1.0'
        danceabilityDictionary.setdefault(key, 0)
        danceabilityDictionary[key] = danceabilityDictionary[key] + 1
    elif danceability > .15:
        key = '.15-.20'
        danceabilityDictionary.setdefault(key, 0)
        danceabilityDictionary[key] = danceabilityDictionary[key] + 1
    elif danceability > .10:
        key = '.10-.15'
        danceabilityDictionary.setdefault(key, 0)
        danceabilityDictionary[key] = danceabilityDictionary[key] + 1
    elif danceability > .05:
        key = '.05-.10'
        danceabilityDictionary.setdefault(key, 0)
        danceabilityDictionary[key] = danceabilityDictionary[key] + 1
    elif danceability > 0:
        key = '0-.05'
        danceabilityDictionary.setdefault(key, 0)
        danceabilityDictionary[key] = danceabilityDictionary[key] + 1
    else:
        key = '0'
        danceabilityDictionary.setdefault(key, 0)
        danceabilityDictionary[key] = danceabilityDictionary[key] + 1

    #HOTNESS
    hotness = float(item[16])
    if hotness > .75:
        hotnessDictionary.setdefault(key, 0)
        hotnessDictionary[key] = hotnessDictionary[key] + 1
    elif hotness > .50:
        key = '.50-.75'
        hotnessDictionary.setdefault(key, 0)
        hotnessDictionary[key] = hotnessDictionary[key] + 1
    elif hotness > .25:
        hotnessDictionary.setdefault(key, 0)
        hotnessDictionary[key] = hotnessDictionary[key] + 1
    else:
        key = '0.0-.25'
        hotnessDictionary.setdefault(key, 0)
        hotnessDictionary[key] = hotnessDictionary[key] + 1


    #TEMPO
    tempo = float(item[17])
    if tempo > 200:
        key = '> 200'
        tempoDictionary.setdefault(key, 0)
        tempoDictionary[key] = tempoDictionary[key] + 1
    elif tempo > 169:
        key = '170-200'
        tempoDictionary.setdefault(key, 0)
        tempoDictionary[key] = tempoDictionary[key] + 1
    elif tempo > 139:
        key = '140-170'
        tempoDictionary.setdefault(key, 0)
        tempoDictionary[key] = tempoDictionary[key] + 1
    elif tempo > 119:
        key = '120-140'
        tempoDictionary.setdefault(key, 0)
        tempoDictionary[key] = tempoDictionary[key] + 1
    elif tempo > 99:
        key = '100-120'
        tempoDictionary.setdefault(key, 0)
        tempoDictionary[key] = tempoDictionary[key] + 1
    elif tempo > 79:
        key = '80-10'
        tempoDictionary.setdefault(key, 0)
        tempoDictionary[key] = tempoDictionary[key] + 1
    else:
        key = '0-80'
        tempoDictionary.setdefault(key, 0)
        tempoDictionary[key] = tempoDictionary[key] + 1


    #LOUDNESS
    loudness = float(item[18])
    if loudness > -5:
        key = '0-(-5)'
        loudnessDictionary.setdefault(key, 0)
        loudnessDictionary[key] = loudnessDictionary[key] + 1
    elif loudness > -10:
        key = '(-5)-(-10)'
        loudnessDictionary.setdefault(key, 0)
        loudnessDictionary[key] = loudnessDictionary[key] + 1
    elif loudness > -50:
        key = '(-10)-(-50)'
        loudnessDictionary.setdefault(key, 0)
        loudnessDictionary[key] = loudnessDictionary[key] + 1
    elif loudness > -100:
        key = '(-50)-(-100)'
        loudnessDictionary.setdefault(key, 0)
        loudnessDictionary[key] = loudnessDictionary[key] + 1
    else:
        key = 'unknown'
        loudnessDictionary.setdefault(key, 0)
        loudnessDictionary[key] = loudnessDictionary[key] + 1

    #LABEL
    label = item[19]
    if "yes" in label:
        key = 'yes'
        labelDictionary.setdefault(key, 0)
        labelDictionary[key] = labelDictionary[key] + 1
    else:
        key = 'no'
        labelDictionary.setdefault(key, 0)
        labelDictionary[key] = labelDictionary[key] + 1
'''


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

# DURATION
print max(durationArray)
print min(durationArray)
for key in durationDictionary:
    print key + "    " + str(durationDictionary[key])

# START OF FADE OUT
for key in danceabilityDictionary:
    print key + "    " + str(danceabilityDictionary[key])


#HOTNESS
for key in hotnessDictionary:
    print key + "    " + str(hotnessDictionary[key])

# TEMPO
for key in tempoDictionary:
    print key + "    " + str(tempoDictionary[key])

#LOUDNESS
for key in loudnessDictionary:
    print key + "    " + str(loudnessDictionary[key])


#LABEL
for key in labelDictionary:
    print key + "    " + str(labelDictionary[key])
'''







