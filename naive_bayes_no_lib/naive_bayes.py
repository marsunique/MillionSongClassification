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

    # Compute probability of a attribute given the label is yes
    def attProbYes(self):
        artistNameDictionary = {}
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
        
        # Count the number
        for item in self.train_data_yes:
            # FIND THE NUMBER OF TIMES AN ARTIST SHOWS UP
            key = item[2]
            artistNameDictionary.setdefault(key, 0)
            artistNameDictionary[key] = artistNameDictionary[key] + 1
            
            # KEY
            if float(item[6]) > .2:
                # Confidence > 0.2
                key = item[5]
                keyDictionary.setdefault(key, 0)
                keyDictionary[key] = keyDictionary[key] + 1
            else:
                key = 'unknown'
                keyDictionary.setdefault(key, 0)
                keyDictionary[key] = keyDictionary[key] + 1

            # TIME SIGNATURE
            if float(item[8]) > .25:
                # Confidence > 0.25
                key = item[7]
                timeSignatureDictionary.setdefault(key, 0)
                timeSignatureDictionary[key] = timeSignatureDictionary[key] + 1
            else:
                key = 'unknown'
                timeSignatureDictionary.setdefault(key, 0)
                timeSignatureDictionary[key] = timeSignatureDictionary[key] + 1

            # MODE
            if float(item[10]) > .25:
                # Confidence > 0.25
                key = item[9]
                modeDictionary.setdefault(key, 0)
                modeDictionary[key] = modeDictionary[key] + 1
            else:
                key = 'unknown'
                modeDictionary.setdefault(key, 0)
                modeDictionary[key] = modeDictionary[key] + 1

            #END OF FADE IN
            fadeIn = float(item[11])
            if fadeIn > 60:
                key = '60+'
                fadeInDictionary.setdefault(key, 0)
                fadeInDictionary[key] = fadeInDictionary[key] + 1
            elif fadeIn > 10:
                key = '10-60'
                fadeInDictionary.setdefault(key, 0)
                fadeInDictionary[key] = fadeInDictionary[key] + 1
            elif fadeIn > 5:
                key = '5-10'
                fadeInDictionary.setdefault(key, 0)
                fadeInDictionary[key] = fadeInDictionary[key] + 1
            elif fadeIn > 1:
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
                key = '.75-1'
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
            elif energy > 0:
                key = '0-.25'
                energyDictionary.setdefault(key, 0)
                energyDictionary[key] = energyDictionary[key] + 1
            else:
                key = 'unknown'
                energyDictionary.setdefault(key, 0)
                energyDictionary[key] = energyDictionary[key] + 1

            #DURATION
            duration = float(item[14])
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
                key = '.20-1'
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
                key = 'unknown'
                danceabilityDictionary.setdefault(key, 0)
                danceabilityDictionary[key] = danceabilityDictionary[key] + 1

            #HOTNESS
            hotness = float(item[16])
            if hotness > .5:
                key = '.5-1'
                hotnessDictionary.setdefault(key, 0)
                hotnessDictionary[key] = hotnessDictionary[key] + 1
            elif hotness >= 0:
                key = '0-.5'
                hotnessDictionary.setdefault(key, 0)
                hotnessDictionary[key] = hotnessDictionary[key] + 1
            else:
                key = 'unknown'
                hotnessDictionary.setdefault(key, 0)
                hotnessDictionary[key] = hotnessDictionary[key] + 1

            #TEMPO
            tempo = float(item[17])
            if tempo > 180:
                key = '180+'
                tempoDictionary.setdefault(key, 0)
                tempoDictionary[key] = tempoDictionary[key] + 1
            elif tempo > 120:
                key = '120-180'
                tempoDictionary.setdefault(key, 0)
                tempoDictionary[key] = tempoDictionary[key] + 1
            elif tempo > 80:
                key = '80-120'
                tempoDictionary.setdefault(key, 0)
                tempoDictionary[key] = tempoDictionary[key] + 1
            else:
                key = '80-'
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
        
        # Calculate conditional probability
        # ARTIST NAME
        for key in artistNameDictionary:
            self.prob_artistName_yes[key] = float(artistNameDictionary[key]) / self.row_number_yes

        # KEY
        for key in keyDictionary:
            self.prob_key_yes[key] = float(keyDictionary[key]) / self.row_number_yes

        # TIME SIGNATURE
        for key in timeSignatureDictionary:
            self.prob_timeSignature_yes[key] = float(timeSignatureDictionary[key]) / self.row_number_yes
        
        # MODE
        for key in modeDictionary:
            self.prob_mode_yes[key] = float(modeDictionary[key]) / self.row_number_yes

        # FADE IN
        for key in fadeInDictionary:
            self.prob_fadeIn_yes[key] = float(fadeInDictionary[key]) / self.row_number_yes

        # FADE OUT
        for key in fadeOutDictionary:
            self.prob_fadeOut_yes[key] = float(fadeOutDictionary[key]) / self.row_number_yes

        # ENERGY
        for key in energyDictionary:
            self.prob_energy_yes[key] = float(energyDictionary[key]) / self.row_number_yes

        # DURATION
        for key in durationDictionary:
            self.prob_duration_yes[key] = float(durationDictionary[key]) / self.row_number_yes

        # DANCEABILITY
        for key in danceabilityDictionary:
            self.prob_danceability_yes[key] = float(danceabilityDictionary[key]) / self.row_number_yes

        # HOTNESS
        for key in hotnessDictionary:
            self.prob_hotness_yes[key] = float(hotnessDictionary[key]) / self.row_number_yes

        # TEMPO
        for key in tempoDictionary:
            self.prob_tempo_yes[key] = float(tempoDictionary[key]) / self.row_number_yes

        # LOUDNESS
        for key in loudnessDictionary:
            self.prob_loudness_yes[key] = float(loudnessDictionary[key]) / self.row_number_yes
        
        #print 'prob_artistName_yes:', self.prob_artistName_yes
        print 'prob_key_yes:', self.prob_key_yes
        print 'prob_timeSignature_yes', self.prob_timeSignature_yes
        print 'prob_mode_yes', self.prob_mode_yes
        print 'prob_fadeIn_yes', self.prob_fadeIn_yes
        print 'prob_fadeOut_yes', self.prob_fadeOut_yes
        print 'prob_energy_yes', self.prob_energy_yes
        print 'prob_duration_yes', self.prob_duration_yes
        print 'prob_danceability_yes', self.prob_danceability_yes
        print 'prob_hotness_yes', self.prob_hotness_yes
        print 'prob_tempo_yes', self.prob_tempo_yes
        print 'prob_loudness_yes', self.prob_loudness_yes

    # Compute probability of a attribute given the label is yes
    def attProbNo(self):
        artistNameDictionary = {}
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
        
        # Count the number
        for item in self.train_data_no:
            # FIND THE NUMBER OF TIMES AN ARTIST SHOWS UP
            key = item[2]
            artistNameDictionary.setdefault(key, 0)
            artistNameDictionary[key] = artistNameDictionary[key] + 1
            
            # KEY
            if float(item[6]) > .2:
                # Confidence > 0.2
                key = item[5]
                keyDictionary.setdefault(key, 0)
                keyDictionary[key] = keyDictionary[key] + 1
            else:
                key = 'unknown'
                keyDictionary.setdefault(key, 0)
                keyDictionary[key] = keyDictionary[key] + 1

            # TIME SIGNATURE
            if float(item[8]) > .25:
                # Confidence > 0.25
                key = item[7]
                timeSignatureDictionary.setdefault(key, 0)
                timeSignatureDictionary[key] = timeSignatureDictionary[key] + 1
            else:
                key = 'unknown'
                timeSignatureDictionary.setdefault(key, 0)
                timeSignatureDictionary[key] = timeSignatureDictionary[key] + 1

            # MODE
            if float(item[10]) > .25:
                # Confidence > 0.25
                key = item[9]
                modeDictionary.setdefault(key, 0)
                modeDictionary[key] = modeDictionary[key] + 1
            else:
                key = 'unknown'
                modeDictionary.setdefault(key, 0)
                modeDictionary[key] = modeDictionary[key] + 1

            #END OF FADE IN
            fadeIn = float(item[11])
            if fadeIn > 60:
                key = '60+'
                fadeInDictionary.setdefault(key, 0)
                fadeInDictionary[key] = fadeInDictionary[key] + 1
            elif fadeIn > 10:
                key = '10-60'
                fadeInDictionary.setdefault(key, 0)
                fadeInDictionary[key] = fadeInDictionary[key] + 1
            elif fadeIn > 5:
                key = '5-10'
                fadeInDictionary.setdefault(key, 0)
                fadeInDictionary[key] = fadeInDictionary[key] + 1
            elif fadeIn > 1:
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
                key = '.75-1'
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
            elif energy > 0:
                key = '0-.25'
                energyDictionary.setdefault(key, 0)
                energyDictionary[key] = energyDictionary[key] + 1
            else:
                key = 'unknown'
                energyDictionary.setdefault(key, 0)
                energyDictionary[key] = energyDictionary[key] + 1

            #DURATION
            duration = float(item[14])
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
                key = '.20-1'
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
                key = 'unknown'
                danceabilityDictionary.setdefault(key, 0)
                danceabilityDictionary[key] = danceabilityDictionary[key] + 1

            #HOTNESS
            hotness = float(item[16])
            if hotness > .5:
                key = '.5-1'
                hotnessDictionary.setdefault(key, 0)
                hotnessDictionary[key] = hotnessDictionary[key] + 1
            elif hotness >= 0:
                key = '0-.5'
                hotnessDictionary.setdefault(key, 0)
                hotnessDictionary[key] = hotnessDictionary[key] + 1
            else:
                key = 'unknown'
                hotnessDictionary.setdefault(key, 0)
                hotnessDictionary[key] = hotnessDictionary[key] + 1

            #TEMPO
            tempo = float(item[17])
            if tempo > 180:
                key = '180+'
                tempoDictionary.setdefault(key, 0)
                tempoDictionary[key] = tempoDictionary[key] + 1
            elif tempo > 120:
                key = '120-180'
                tempoDictionary.setdefault(key, 0)
                tempoDictionary[key] = tempoDictionary[key] + 1
            elif tempo > 80:
                key = '80-120'
                tempoDictionary.setdefault(key, 0)
                tempoDictionary[key] = tempoDictionary[key] + 1
            else:
                key = '80-'
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
        
        # Calculate conditional probability
        # ARTIST NAME
        for key in artistNameDictionary:
            self.prob_artistName_no[key] = float(artistNameDictionary[key]) / self.row_number_no

        # KEY
        for key in keyDictionary:
            self.prob_key_no[key] = float(keyDictionary[key]) / self.row_number_no

        # TIME SIGNATURE
        for key in timeSignatureDictionary:
            self.prob_timeSignature_no[key] = float(timeSignatureDictionary[key]) / self.row_number_no
        
        # MODE
        for key in modeDictionary:
            self.prob_mode_no[key] = float(modeDictionary[key]) / self.row_number_no

        # FADE IN
        for key in fadeInDictionary:
            self.prob_fadeIn_no[key] = float(fadeInDictionary[key]) / self.row_number_no

        # FADE OUT
        for key in fadeOutDictionary:
            self.prob_fadeOut_no[key] = float(fadeOutDictionary[key]) / self.row_number_no

        # ENERGY
        for key in energyDictionary:
            self.prob_energy_no[key] = float(energyDictionary[key]) / self.row_number_no

        # DURATION
        for key in durationDictionary:
            self.prob_duration_no[key] = float(durationDictionary[key]) / self.row_number_no

        # DANCEABILITY
        for key in danceabilityDictionary:
            self.prob_danceability_no[key] = float(danceabilityDictionary[key]) / self.row_number_no

        # HOTNESS
        for key in hotnessDictionary:
            self.prob_hotness_no[key] = float(hotnessDictionary[key]) / self.row_number_no

        # TEMPO
        for key in tempoDictionary:
            self.prob_tempo_no[key] = float(tempoDictionary[key]) / self.row_number_no

        # LOUDNESS
        for key in loudnessDictionary:
            self.prob_loudness_no[key] = float(loudnessDictionary[key]) / self.row_number_no
        
        #print 'prob_artistName_no:', self.prob_artistName_no
        print 'prob_key_no:', self.prob_key_no
        print 'prob_timeSignature_no', self.prob_timeSignature_no
        print 'prob_mode_no', self.prob_mode_no
        print 'prob_fadeIn_no', self.prob_fadeIn_no
        print 'prob_fadeOut_no', self.prob_fadeOut_no
        print 'prob_energy_no', self.prob_energy_no
        print 'prob_duration_no', self.prob_duration_no
        print 'prob_danceability_no', self.prob_danceability_no
        print 'prob_hotness_no', self.prob_hotness_no
        print 'prob_tempo_no', self.prob_tempo_no
        print 'prob_loudness_no', self.prob_loudness_no


    def main(self):
        self.readData()
        self.attProbYes()
        self.attProbNo()



if __name__ == '__main__':
    nb_model = NaiveBayes()
    nb_model.main()

