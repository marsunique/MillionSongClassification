#-*- coding: utf-8 -*-
import time

class NaiveBayes(object):
    def __init__(self, train_data):
        # timestamp
        self.train_start_time = 0
        self.train_end_time = 0
        # training data
        self.train_data_path = train_data
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
                line = line.strip().split(',')
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
        print 'Total number of trainning data:', self.total_row
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
            else:
                key = 'unknown'
            keyDictionary.setdefault(key, 0)
            keyDictionary[key] = keyDictionary[key] + 1

            # TIME SIGNATURE
            if float(item[8]) > .25:
                # Confidence > 0.25
                key = item[7]
            else:
                key = 'unknown'
            timeSignatureDictionary.setdefault(key, 0)
            timeSignatureDictionary[key] = timeSignatureDictionary[key] + 1

            # MODE
            if float(item[10]) > .25:
                # Confidence > 0.25
                key = item[9]
            else:
                key = 'unknown'
            modeDictionary.setdefault(key, 0)
            modeDictionary[key] = modeDictionary[key] + 1

            #END OF FADE IN
            fadeIn = float(item[11])
            if fadeIn > 60:
                key = '60+'
            elif fadeIn > 10:
                key = '10-60'
            elif fadeIn > 5:
                key = '5-10'
            elif fadeIn > 1:
                key = '1-5'
            else:
                key = '1-'
            fadeInDictionary.setdefault(key, 0)
            fadeInDictionary[key] = fadeInDictionary[key] + 1

            #FADE OUT TIME
            fadeOut = float(item[14]) - float(item[12])
            if fadeOut > 60:
                key = '60+'
            elif fadeOut > 10:
                key = '10-60'
            elif fadeOut > 1:
                key = '1-10'
            else:
                key = '1-'
            fadeOutDictionary.setdefault(key, 0)
            fadeOutDictionary[key] = fadeOutDictionary[key] + 1

            #ENERGY
            energy = float(item[13])
            if energy > .75:
                key = '.75-1'
            elif energy > .50:
                key = '.50-.75'
            elif energy > .25:
                key = '.25-.50'
            elif energy > 0:
                key = '0-.25'
            else:
                key = 'unknown'
            energyDictionary.setdefault(key, 0)
            energyDictionary[key] = energyDictionary[key] + 1

            #DURATION
            duration = float(item[14])
            if duration > 480:
                key = '480+'
            elif duration > 270:
                key = '270-480'
            elif duration > 120:
                key = '120-270'
            elif duration > 10:
                key = '10-120'
            else:
                key = '10-'
            durationDictionary.setdefault(key, 0)
            durationDictionary[key] = durationDictionary[key] + 1

            #DANCEABILITY
            danceability = float(item[15])
            if danceability > .20:
                key = '.20-1'
            elif danceability > .15:
                key = '.15-.20'
            elif danceability > .10:
                key = '.10-.15'
            elif danceability > .05:
                key = '.05-.10'
            elif danceability > 0:
                key = '0-.05'
            else:
                key = 'unknown'
            danceabilityDictionary.setdefault(key, 0)
            danceabilityDictionary[key] = danceabilityDictionary[key] + 1

            #HOTNESS
            hotness = float(item[16])
            if hotness > .5:
                key = '.5-1'
            elif hotness >= 0:
                key = '0-.5'
            else:
                key = 'unknown'
            hotnessDictionary.setdefault(key, 0)
            hotnessDictionary[key] = hotnessDictionary[key] + 1

            #TEMPO
            tempo = float(item[17])
            if tempo > 180:
                key = '180+'
            elif tempo > 120:
                key = '120-180'
            elif tempo > 80:
                key = '80-120'
            else:
                key = '80-'
            tempoDictionary.setdefault(key, 0)
            tempoDictionary[key] = tempoDictionary[key] + 1

            #LOUDNESS
            loudness = float(item[18])
            if loudness > -5:
                key = '0-(-5)'
            elif loudness > -10:
                key = '(-5)-(-10)'
            elif loudness > -50:
                key = '(-10)-(-50)'
            elif loudness > -100:
                key = '(-50)-(-100)'
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
        
        '''
        print 'prob_artistName_yes:', self.prob_artistName_yes
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
        '''

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
        
        '''
        print 'prob_artistName_no:', self.prob_artistName_no
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
        '''


    def main(self):
        self.train_start_time = time.time()
        self.readData()
        self.attProbYes()
        self.attProbNo()
        self.train_end_time = time.time()


class Predict(object):
    def __init__(self, nb_model, test_data):
        # timestamp
        self.pred_start_time = 0
        self.pred_end_time = 0
        # class variables
        self.model = nb_model
        self.test_data_path = test_data
        self.result_label = []
        self.total_row = 0
        # build model
        self.model.main()
        # contingency table elements
        self.yes_yes_count = 0
        self.yes_no_count = 0
        self.no_yes_count = 0
        self.no_no_count = 0

    def predict(self):
        with open(self.test_data_path, 'r+') as openFile:
            count = 0
            for line in openFile:
                count += 1
                if count == 1:
                    continue
                line = line.strip().split(',')
                # init probability of each attribute
                # ARTIST NAME
                p_artistName_yes = 0
                p_artistName_no = 0
                # KEY
                p_key_yes = 0
                p_key_no = 0
                # TIME SIGNATURE
                p_timeSignature_yes = 0
                p_timeSignature_no = 0
                # MODE
                p_mode_yes = 0
                p_mode_no = 0
                # FADE IN
                p_fadeIn_yes = 0
                p_fadeIn_no = 0
                # FADE OUT
                p_fadeOut_yes = 0
                p_fadeOut_no = 0
                # ENERGY (not used)
                # p_energy_yes = 0
                # p_energy_no = 0
                # DURATION
                p_duration_yes = 0
                p_duration_no = 0
                # DANCEABILITY (not used)
                # p_danceability_yes = 0
                # p_danceability_no = 0
                # HOTNESS
                p_hotness_yes = 0
                p_hotness_no = 0
                # TEMPO
                p_tempo_yes = 0
                p_tempo_no = 0
                # LOUDNESS
                p_loudness_yes = 0
                p_loudness_no = 0

                # look up the probability for each attribute
                # ARTIST
                key = line[2]
                # This artist shows up in both yes and no category from training data
                if (key in self.model.prob_artistName_yes) and (key in self.model.prob_artistName_no):
                    p_artistName_yes = self.model.prob_artistName_yes[key]
                    p_artistName_no = self.model.prob_artistName_no[key]
                # This artist shows up only in yes category from training data
                elif (key in self.model.prob_artistName_yes) and not (key in self.model.prob_artistName_no):
                    p_artistName_yes = float(2)
                    p_artistName_no = float(1)
                # This artist shows up only in no category from training data
                elif not (key in self.model.prob_artistName_yes) and (key in self.model.prob_artistName_no):
                    p_artistName_yes = float(1)
                    p_artistName_no = float(2)
                # This artist shows up in neither yes nor no category from training data
                else:
                    p_artistName_yes = float(1)
                    p_artistName_no = float(1)

                # KEY
                if float(line[6]) > .2:
                    # Confidence > 0.2
                    key = line[5]
                else:
                    key = 'unknown'
                p_key_yes = self.model.prob_key_yes[key]
                p_key_no = self.model.prob_key_no[key]
                
                # TIME SIGNATURE
                if float(line[8]) > .25:
                    # Confidence > 0.25
                    key = line[7]
                else:
                    key = 'unknown'
                p_timeSignature_yes = self.model.prob_timeSignature_yes[key]
                p_timeSignature_no = self.model.prob_timeSignature_no[key]
                
                # MODE
                if float(line[10]) > .25:
                    # Confidence > 0.25
                    key = line[9]
                else:
                    key = 'unknown'
                p_mode_yes = self.model.prob_mode_yes[key]
                p_mode_no = self.model.prob_mode_no[key]
                
                # END OF FADE IN
                fadeIn = float(line[11])
                if fadeIn > 60:
                    key = '60+'
                elif fadeIn > 10:
                    key = '10-60'
                elif fadeIn > 5:
                    key = '5-10'
                elif fadeIn > 1:
                    key = '1-5'
                else:
                    key = '1-'
                # This fadeIn shows up in both yes and no category from training data
                if (key in self.model.prob_fadeIn_yes) and (key in self.model.prob_fadeIn_no):
                    p_fadeIn_yes = self.model.prob_fadeIn_yes[key]
                    p_fadeIn_no = self.model.prob_fadeIn_no[key]
                # This fadeIn shows up only in yes category from training data
                elif (key in self.model.prob_fadeIn_yes) and not (key in self.model.prob_fadeIn_no):
                    p_fadeIn_yes = float(2)
                    p_fadeIn_no = float(1)
                # This fadeIn shows up only in no category from training data
                elif not (key in self.model.prob_fadeIn_yes) and (key in self.model.prob_fadeIn_no):
                    p_fadeIn_yes = float(1)
                    p_fadeIn_no = float(2)
                # This fadeIn shows up in neither yes nor no category from training data
                else:
                    p_fadeIn_yes = float(1)
                    p_fadeIn_no = float(1)

                # FADE OUT TIME
                fadeOut = float(line[14]) - float(line[12])
                if fadeIn > 60:
                    key = '60+'
                elif fadeIn > 10:
                    key = '10-60'
                elif fadeIn > 1:
                    key = '1-10'
                else:
                    key = '1-'
                # This fadeOut shows up in both yes and no category from training data
                if (key in self.model.prob_fadeOut_yes) and (key in self.model.prob_fadeOut_no):
                    p_fadeOut_yes = self.model.prob_fadeOut_yes[key]
                    p_fadeOut_no = self.model.prob_fadeOut_no[key]
                # This fadeOut shows up only in yes category from training data
                elif (key in self.model.prob_fadeOut_yes) and not (key in self.model.prob_fadeOut_no):
                    p_fadeOut_yes = float(2)
                    p_fadeOut_no = float(1)
                # This fadeOut shows up only in no category from training data
                elif not (key in self.model.prob_fadeOut_yes) and (key in self.model.prob_fadeOut_no):
                    p_fadeOut_yes = float(1)
                    p_fadeOut_no = float(2)
                # This fadeOut shows up in neither yes nor no category from training data
                else:
                    p_fadeOut_yes = float(1)
                    p_fadeOut_no = float(1)
                
                # ENERGY (not used)
                '''
                energy = float(line[13])
                if energy > .75:
                    key = '.75-1'
                elif energy > .50:
                    key = '.50-.75'
                elif energy > .25:
                    key = '.25-.50'
                elif energy > 0:
                    key = '0-.25'
                else:
                    key = 'unknown'
                # This energy shows up in both yes and no category from training data
                if (key in self.model.prob_energy_yes) and (key in self.model.prob_energy_no):
                    p_energy_yes = self.model.prob_energy_yes[key]
                    p_energy_no = self.model.prob_energy_no[key]
                # This energy shows up only in yes category from training data
                elif (key in self.model.prob_energy_yes) and not (key in self.model.prob_energy_no):
                    p_energy_yes = float(2)
                    p_energy_no = float(1)
                # This energy shows up only in no category from training data
                elif not (key in self.model.prob_energy_yes) and (key in self.model.prob_energy_no):
                    p_energy_yes = float(1)
                    p_energy_no = float(2)
                # This energy shows up in neither yes nor no category from training data
                else:
                    p_energy_yes = float(1)
                    p_energy_no = float(1)
                '''

                # DURATION
                duration = float(line[14])
                if duration > 480:
                    key = '480+'
                elif duration > 270:
                    key = '270-480'
                elif duration > 120:
                    key = '120-270'
                elif duration > 10:
                    key = '10-120'
                else:
                    key = '10-'
                # This duration shows up in both yes and no category from training data
                if (key in self.model.prob_duration_yes) and (key in self.model.prob_duration_no):
                    p_duration_yes = self.model.prob_duration_yes[key]
                    p_duration_no = self.model.prob_duration_no[key]
                # This duration shows up only in yes category from training data
                elif (key in self.model.prob_duration_yes) and not (key in self.model.prob_duration_no):
                    p_duration_yes = float(2)
                    p_duration_no = float(1)
                # This duration shows up only in no category from training data
                elif not (key in self.model.prob_duration_yes) and (key in self.model.prob_duration_no):
                    p_duration_yes = float(1)
                    p_duration_no = float(2)
                # This duration shows up in neither yes nor no category from training data
                else:
                    p_duration_yes = float(1)
                    p_duration_no = float(1)
                
                # DANCEABILITY (not used)
                '''
                danceability = float(line[15])
                if danceability > .20:
                    key = '.20-1'
                elif danceability > .15:
                    key = '.15-.20'
                elif danceability > .10:
                    key = '.10-.15'
                elif danceability > .05:
                    key = '.05-.10'
                elif danceability > 0:
                    key = '0-.05'
                else:
                    key = 'unknown'
                # This danceability shows up in both yes and no category from training data
                if (key in self.model.prob_danceability_yes) and (key in self.model.prob_danceability_no):
                    p_danceability_yes = self.model.prob_danceability_yes[key]
                    p_danceability_no = self.model.prob_danceability_no[key]
                # This danceability shows up only in yes category from training data
                elif (key in self.model.prob_danceability_yes) and not (key in self.model.prob_danceability_no):
                    p_danceability_yes = float(2)
                    p_danceability_no = float(1)
                # This danceability shows up only in no category from training data
                elif not (key in self.model.prob_danceability_yes) and (key in self.model.prob_danceability_no):
                    p_danceability_yes = float(1)
                    p_danceability_no = float(2)
                # This danceability shows up in neither yes nor no category from training data
                else:
                    p_danceability_yes = float(1)
                    p_danceability_no = float(1)
                '''

                #HOTNESS
                hotness = float(line[16])
                if hotness > .5:
                    key = '.5-1'
                elif hotness >= 0:
                    key = '0-.5'
                else:
                    key = 'unknown'
                # This hotness shows up in both yes and no category from training data
                if (key in self.model.prob_hotness_yes) and (key in self.model.prob_hotness_no):
                    p_hotness_yes = self.model.prob_hotness_yes[key]
                    p_hotness_no = self.model.prob_hotness_no[key]
                # This hotness shows up only in yes category from training data
                elif (key in self.model.prob_hotness_yes) and not (key in self.model.prob_hotness_no):
                    p_hotness_yes = float(2)
                    p_hotness_no = float(1)
                # This hotness shows up only in no category from training data
                elif not (key in self.model.prob_hotness_yes) and (key in self.model.prob_hotness_no):
                    p_hotness_yes = float(1)
                    p_hotness_no = float(2)
                # This hotness shows up in neither yes nor no category from training data
                else:
                    p_hotness_yes = float(1)
                    p_hotness_no = float(1)

                #TEMPO
                tempo = float(line[17])
                if tempo > 180:
                    key = '180+'
                elif tempo > 120:
                    key = '120-180'
                elif tempo > 80:
                    key = '80-120'
                else:
                    key = '80-'
                # This tempo shows up in both yes and no category from training data
                if (key in self.model.prob_tempo_yes) and (key in self.model.prob_tempo_no):
                    p_tempo_yes = self.model.prob_tempo_yes[key]
                    p_tempo_no = self.model.prob_tempo_no[key]
                # This tempo shows up only in yes category from training data
                elif (key in self.model.prob_tempo_yes) and not (key in self.model.prob_tempo_no):
                    p_tempo_yes = float(2)
                    p_tempo_no = float(1)
                # This tempo shows up only in no category from training data
                elif not (key in self.model.prob_tempo_yes) and (key in self.model.prob_tempo_no):
                    p_tempo_yes = float(1)
                    p_tempo_no = float(2)
                # This tempo shows up in neither yes nor no category from training data
                else:
                    p_tempo_yes = float(1)
                    p_tempo_no = float(1)

                #LOUDNESS
                loudness = float(line[18])
                if loudness > -5:
                    key = '0-(-5)'
                elif loudness > -10:
                    key = '(-5)-(-10)'
                elif loudness > -50:
                    key = '(-10)-(-50)'
                elif loudness > -100:
                    key = '(-50)-(-100)'
                else:
                    key = 'unknown'
                # This loudness shows up in both yes and no category from training data
                if (key in self.model.prob_loudness_yes) and (key in self.model.prob_loudness_no):
                    p_loudness_yes = self.model.prob_loudness_yes[key]
                    p_loudness_no = self.model.prob_loudness_no[key]
                # This loudness shows up only in yes category from training data
                elif (key in self.model.prob_loudness_yes) and not (key in self.model.prob_loudness_no):
                    p_loudness_yes = float(2)
                    p_loudness_no = float(1)
                # This loudness shows up only in no category from training data
                elif not (key in self.model.prob_loudness_yes) and (key in self.model.prob_loudness_no):
                    p_loudness_yes = float(1)
                    p_loudness_no = float(2)
                # This loudness shows up in neither yes nor no category from training data
                else:
                    p_loudness_yes = float(1)
                    p_loudness_no = float(1)
                

                # Compute P(X|c)P(c)
                p_x_yes = p_artistName_yes * p_key_yes * p_timeSignature_yes * p_mode_yes *\
                            p_fadeIn_yes * p_fadeOut_yes * p_duration_yes * p_hotness_yes *\
                            p_tempo_yes * p_loudness_yes * self.model.prob_yes
                
                p_x_no = p_artistName_no * p_key_no * p_timeSignature_no * p_mode_no *\
                            p_fadeIn_no * p_fadeOut_no * p_duration_no * p_hotness_no *\
                            p_tempo_no * p_loudness_no * self.model.prob_no
                
                original_label = line[19]
                if p_x_yes >= p_x_no:
                    self.result_label.append('yes')
                    if original_label == 'yes':
                        self.yes_yes_count += 1
                    else:
                        self.no_yes_count += 1
                else:
                    self.result_label.append('no')
                    if original_label == 'yes':
                        self.yes_no_count += 1
                    else:
                        self.no_no_count += 1
            
        openFile.close()
        self.total_row = count-1
        print 'Total number of test data', self.total_row

    def analyze(self):
        print 'yes:', self.yes_yes_count + self.no_yes_count
        print 'no:', self.yes_no_count + self.no_no_count
        print '\nContingency Table\n'
        print '----------------------------------------------------'
        print '|   ori\\pred   |       yes       |       no        |'
        print '----------------------------------------------------'
        print '|      yes     |       %d       |       %d       |' % (self.yes_yes_count, self.yes_no_count)
        print '----------------------------------------------------'
        print '|      no      |       %d       |      %d      |' % (self.no_yes_count, self.no_no_count)
        print '----------------------------------------------------'

        print 'Overall Accuracy:', (self.yes_yes_count + self.no_no_count) / float(self.total_row)
        print 'Accuracy for \'yes\' Class (Precision):', float(self.yes_yes_count) / (self.yes_yes_count + self.no_yes_count)
        print 'Accuracy for \'no\' Class:', float(self.no_no_count) / (self.no_no_count + self.yes_no_count)
        print 'Recall:', float(self.yes_yes_count) / (self.yes_yes_count + self.yes_no_count)
        print 'Specificity:', float(self.no_no_count) / (self.no_no_count + self.no_yes_count)
        print 'F-measure:', float(2 * self.yes_yes_count) / (2 * self.yes_yes_count + self.yes_no_count + self.no_yes_count)

    def run(self):
        print '\nFollowing is the prediction result\n'
        self.pred_start_time = time.time()
        self.predict()
        self.pred_end_time = time.time()
        self.analyze()


if __name__ == '__main__':
    nb_model = NaiveBayes('train_sample.csv')
    pred = Predict(nb_model, 'test_sample.csv')
    pred.run()
    print '\nTraining Time:', nb_model.train_end_time - nb_model.train_start_time
    print 'Prediction Time:', pred.pred_end_time - pred.pred_start_time

