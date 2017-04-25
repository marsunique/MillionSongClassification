# I used the hdf5_getters library, so I felt inclined to leave this comment stamp

"""
Thierry Bertin-Mahieux (2010) Columbia University
tb2332@columbia.edu
Code to quickly see the content of an HDF5 file.
This is part of the Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.
Copyright 2010, Thierry Bertin-Mahieux
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import hdf5_getters
import numpy as np
import json


class songData:
    
    #def __init__(self):
    #    self.name = "name"
    def __init__(self,name):
        self.name = name
    
    '''
    def __init__(self, 
                    new_analysis_sample_rate,
                    new_artist_7digitalid,
                    new_artist_familiarity,
                    new_artist_hotttnesss,
                    new_artist_id,
                    new_artist_latitude,
                    new_artist_location,
                    new_artist_longitude,
                    new_artist_mbid,
                    new_artist_mbtags,
                    new_artist_mbtags_count,
                    new_artist_name,
                    new_artist_playmeid,
                    new_artist_terms,
                    new_artist_terms_freq,
                    new_artist_terms_weight,
                    new_audio_md5,
                    new_bars_confidence,
                    new_bars_start,
                    new_beats_confidence,
                    new_beats_start,
                    new_danceability,
                    new_duration,
                    new_end_of_fade_in,
                    new_energy,
                    new_key,
                    new_key_confidence,
                    new_loudness,
                    new_mode,
                    new_mode_confidence,
                    new_release,
                    new_release_7digitalid,
                    new_sections_confidence,
                    new_sections_start,
                    new_segments_confidence,
                    new_segments_loudness_max,
                    new_segments_loudness_max_time,
                    new_segments_loudness_start,
                    new_segments_pitches,
                    new_segments_start,
                    new_segments_timbre,
                    new_similar_artists,
                    new_song_hotttnesss,
                    new_song_id,
                    new_start_of_fade_out,
                    new_tatums_confidence,
                    new_tatums_start,
                    new_tempo,
                    new_time_signature,
                    new_time_signature_confidence,
                    new_title,
                    new_track_7digitalid,
                    new_track_id,
                    new_year):
        self.analysis_sample_rate = new_analysis_sample_rate
        self.artist_7digitalid = new_artist_7digitalid
        self.artist_familiarity = new_artist_familiarity
        self.artist_hotttnesss = new_artist_hotttnesss
        self.artist_id = new_artist_id
        self.new_artist_latitude = new_artist_latitude
        self.artist_location = new_artist_location
        self.artist_longitude = new_artist_longitude
        self.artist_mbid = new_artist_mbid
        self.artist_mbtags = new_artist_mbtags
        self.artist_mbtags_count = new_artist_mbtags_count
        self.artist_name = new_artist_name
        self.artist_playmeid = new_artist_playmeid
        self.artist_terms = new_artist_terms
        self.artist_terms_freq = new_artist_terms_freq
        self.artist_terms_weight = new_artist_terms_weight
        self.audio_md5 = new_audio_md5
        self.bars_confidence = new_bars_confidence
        self.bars_start = new_bars_start
        self.beats_confidence = new_beats_confidence
        self.beats_start = new_beats_start
        self.danceability = new_danceability
        self.duration = new_duration
        self.end_of_fade_in = new_end_of_fade_in
        self.energy = new_energy
        self.key = new_key
        self.key_confidence = new_key_confidence
        self.loudness = new_loudness
        self.mode = new_mode
        self.mode_confidence = new_mode_confidence
        self.release = new_release
        self.release_7digitalid = new_release_7digitalid
        self.sections_confidence = new_sections_confidence
        self.new_sections_start = new_sections_start
        self.segments_confidence = new_segments_confidence
        self.segments_loudness_max = new_segments_loudness_max
        self.segments_loudness_max_time = new_segments_loudness_max_time
        self.segments_loudness_start = new_segments_loudness_start
        self.segments_pitches = new_segments_pitches
        self.segments_start = new_segments_start
        self.segments_timbre = new_segments_timbre
        self.similar_artists = new_similar_artists
        self.song_hotttnesss = new_song_hotttnesss
        self.song_id = new_song_id
        self.start_of_fade_out = new_start_of_fade_out
        self.tatums_confidence  = new_tatums_confidence
        self.tatums_start = new_tatums_start
        self.tempo = new_tempo
        self.time_signature = new_time_signature
        self.time_signature_confidence = new_time_signature_confidence
        self.title = new_title
        self.track_7digitalid = new_track_7digitalid
        self.track_id = new_track_id
        self.year = new_year   
    '''
    
    #no shapes
    def __init__(self,
                new_artist_mbid,
                new_artist_name,
                new_artist_playmeid,
                new_artist_audio_md_five,
                new_danceability,
                new_duration,
                new_end_of_fade_in,
                new_energy,
                new_key,
                new_key_confidence,
                new_loudness,
                new_mode,
                new_mode_confidence,
                new_release,
                new_release_seven_digital_id,
                new_song_hottness,
                new_song_id,
                new_start_of_fade_out,
                new_tempo,
                new_time_signature,
                new_time_signature_confidence,
                new_title,
                new_track_seven_digital_id,
                new_track_id,
                new_year):
        self.artist_mbid = str(new_artist_mbid)
        self.artist_name = str(new_artist_name)
        self.artist_playmeid = int(new_artist_playmeid)
        self.artist_audio_md_five = str(new_artist_audio_md_five)
        self.danceability = float(new_danceability)
        self.duration = float(new_duration)
        self.end_of_fade_in = float(new_end_of_fade_in)
        self.energy = float(new_energy)
        self.key = int(new_key)
        self.key_confidence = float(new_key_confidence)
        self.loudness = float(new_loudness)
        self.mode = int(new_mode)
        self.mode_confidence = float(new_mode_confidence)
        self.release = str(new_release)
        self.release_seven_digital_id = int(new_release_seven_digital_id)
        self.song_hottness = float(new_song_hottness)
        self.song_id = str(new_song_id)
        self.start_of_fade_out = float(new_start_of_fade_out)
        self.tempo = float(new_tempo)
        self.time_signature = int(new_time_signature)
        self.time_signature_confidence = float(new_time_signature_confidence)
        self.title = str(new_title)
        self.track_seven_digital_id = str(new_track_seven_digital_id)
        self.track_id = str(new_track_id)
        self.year = int(new_year)
    
    
    def serialize(self):
        return {
            '''
            "artist_audio_md_five": self.artist_audio_md_five,
            "artist_mbid": self.artist_mbid,
            "artist_name": self.artist_name,
            "artist_playmeid": self.artist_playmeid,
            
            "danceability": self.danceability,
            "duration": self.duration,
            "end_of_fade_in": self.end_of_fade_in,
            "energy": self.energy,
            "key": self.key,
            "key_confidence": self.key_confidence,
            "loudness": self.loudness,
            "mode": self.mode,
            "mode_confidence": self.mode_confidence,
            "release": self.release,
            "release_seven_digital_id": self.release_seven_digital_id,
            
            "song_hottness": self.song_hottness,
            "song_id": self.song_id,
            "start_of_fade_out": self.start_of_fade_out,
            "tempo": self.tempo,
            "time_signature": self.time_signature,
            "time_signature_confidence": self.time_signature_confidence,
            "title": self.title,
            "track_id": self.track_id,
            "track_seven_digital_id": self.track_seven_digital_id,
            "year": self.year
            '''
            
            '''
            "analysis_sample_rate" : self.analysis_sample_rate,
            "artist_7digitalid" : self.artist_7digitalid,
            "artist_familiarity" : self.artist_familiarity,
            "artist_hotttnesss" : self.artist_hotttnesss,
            "artist_id" : self.artist_id,
            "artist_latitude" : self.artist_latitude,
            "artist_location" : self.artist_location,
            "artist_longitude" : self.artist_longitude,
            "artist_mbid": self.artist_mbid,
            "artist_mbtags" : self.artist_mbtags,
            "artist_mbtags_count" : self.artist_mbtags_count,
            "artist_name": self.artist_name,
            "artist_playmeid": self.artist_playmeid,
            "artist_terms" : self.artist_terms,
            "artist_terms_freq" : self.artist_terms_freq,
            "artist_terms_weight" : self.artist_terms_weight,
            "artist_audio_md_five": self.artist_audio_md_five,
            "bars_confidence" : self.bars_confidence,
            "bars_start" : self.bars_start,
            "beats_confidence" : self.beats_confidence,
            "beats_start" : self.beats_start,
            
            "danceability": self.danceability,
            "duration": self.duration,
            "end_of_fade_in": self.end_of_fade_in,
            "energy": self.energy,
            "key": self.key,
            "key_confidence": self.key_confidence,
            "loudness": self.loudness,
            "mode": self.mode,
            "mode_confidence": self.mode_confidence,
            "release": self.release,
            "release_seven_digital_id": self.release_seven_digital_id,
            
            "sections_confidence" : self.sections_confidence,
            "segments_confidence" : self.segments_confidence,
            "segments_loudness_max" : self.segments_loudness_max,
            "segments_loudness_max_time" : self.segments_loudness_max_time,
            "segments_loudness_start" : self.segments_loudness_start,
            "segments_pitches" : self.segments_pitches,
            "segments_start" : self.segments_start,
            "segments_timbre" : self.segments_timbre,
            "similar_artists" : self.similar_artists,

            "song_hottness": self.song_hottness,
            "song_id" : self.song_id,
            "start_of_fade_out" : self.start_of_fade_out,
            "tatums_confidence" : self.tatums_confidence,
            "tatums_start" : self.tatums_start,
            "tempo" : self.tempo,
            "time_signature" : self.time_signature,
            "time_signature_confidence" : self.time_signature_confidence,
            "title" : self.title,
            "track_id" : self.track_id,
            "track_seven_digital_id" : self.track_seven_digital_id,
            
            "year": self.year
            '''
        }

        
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


if __name__ == '__main__':
    """ MAIN """
    
    
    #todo: D G V
    letters = ["D", "G", "V"]
    #hdf5path = "/Volumes/DUSTIN/A/A/A/TRAAAAK128F931876.h5"
    for letter in letters:
        masterList = []
        totalCount = 0
        h5files = [os.path.join(root, name)
                     for root, dirs, files in os.walk("/Volumes/DUSTIN/Million/" + letter + "/")
                     for name in files
                     if name.endswith((".h5"))]
        print str(len(h5files)) + " total files in " + letter

        for file in h5files:
            totalCount = totalCount + 1
            if totalCount % 1000 == 0:
                print letter + "totalCount = " + str(totalCount) + "   |    List length = " + str(len(masterList))
            # sanity check
            if not os.path.isfile(file):
                continue
            
            h5 = hdf5_getters.open_h5_file_read(file)
            numSongs = hdf5_getters.get_num_songs(h5)
            #print numSongs
            # get all getters
            getters = filter(lambda x: x[:4] == 'get_', hdf5_getters.__dict__.keys())
            getters.remove("get_num_songs") # special case
            '''
                if onegetter == 'num_songs' or onegetter == 'get_num_songs':
                getters = []
                elif onegetter != '':
                if onegetter[:4] != 'get_':
                    onegetter = 'get_' + onegetter
                    try:
                    getters.index(onegetter)
                    except ValueError:
                    #print 'ERROR: getter requested:',onegetter,'does not exist.'
                    h5.close()
                    sys.exit(0)
                    getters = [onegetter]
            '''

            getters = np.sort(getters)
        
            for i in range(0,numSongs):
                #if i % 500 == 0 :
                #    print "iteration : " + str(i)

                '''
                try:
                    asr = hdf5_getters.__getattribute__(getters[0])(h5,i)
                except AttributeError, e:
                    asr = None
                #print asr

                try:
                    asdid = hdf5_getters.__getattribute__(getters[1])(h5,i)
                except AttributeError, e:
                    asdid = None        
                #print asdid

                try:    
                    af = hdf5_getters.__getattribute__(getters[2])(h5,i)
                except AttributeError, e:
                    af = None
                #print af

                try:
                    ah = hdf5_getters.__getattribute__(getters[3])(h5,i)
                except AttributeError, e:            
                    ah = None
                #print ah

                try:
                    aid = hdf5_getters.__getattribute__(getters[4])(h5,i)
                except AttributeError, e:
                    aid = None   
                #print aid

                try:
                    alat = hdf5_getters.__getattribute__(getters[5])(h5,i)
                except AttributeError, e:
                    alat = None
                #print alat
                    
                try:
                    aloc = hdf5_getters.__getattribute__(getters[6])(h5,i)
                except AttributeError, e:
                    aloc = None
                #print aloc

                try:
                    alon = hdf5_getters.__getattribute__(getters[7])(h5,i)
                except AttributeError, e:
                    alon = None
                #print alon
                '''
                try:
                    ambid = str(hdf5_getters.__getattribute__(getters[8])(h5,i))
                except AttributeError, e:
                    ambid = None
                #print "ambid" + str(ambid)
                


                '''
                try:
                    ambtag = hdf5_getters.__getattribute__(getters[9])(h5,i)
                except AttributeError, e:
                    ambtag = None
                #print ambtag

                try:
                    ambtagc = hdf5_getters.__getattribute__(getters[10])(h5,i)
                except AttributeError, e:
                    ambtagc = None
                #print ambtagc
                '''

                try:
                    aname = str(hdf5_getters.__getattribute__(getters[11])(h5,i))
                except AttributeError, e:
                    aname = None
                #print aname

                try:
                    apmeid = int(hdf5_getters.__getattribute__(getters[12])(h5,i))
                except AttributeError, e:
                    apmeid = None
                #print apmeid
                '''
                try:
                    at = hdf5_getters.__getattribute__(getters[13])(h5,i)
                except AttributeError, e:
                    at = None
                #print at        

                try:
                    atf = hdf5_getters.__getattribute__(getters[14])(h5,i)
                except AttributeError, e:
                    atf = None
                #print atf        

                try:
                    atw = hdf5_getters.__getattribute__(getters[15])(h5,i)
                except AttributeError, e:
                    atw = []
                #print atw        

                '''
                try:
                    amdfive = str(hdf5_getters.__getattribute__(getters[16])(h5,i))
                except AttributeError, e:
                    amdfive = None
                #print amdfive

                '''
                try:
                    baconf = hdf5_getters.__getattribute__(getters[17])(h5,i)
                except AttributeError, e:
                    baconf = None
                #print baconf
                
                try:
                    bastart = hdf5_getters.__getattribute__(getters[18])(h5,i)
                except AttributeError, e:
                    bastart = None
                #print bastart
                
                try:
                    beconf = hdf5_getters.__getattribute__(getters[19])(h5,i)
                except AttributeError, e:
                    beconf = None
                #print beconf
         
                try:
                    bestart = asdid = hdf5_getters.__getattribute__(getters[20])(h5,i)
                except AttributeError, e:
                    bestart = None
                #print bestart        
                '''
                try:
                    dance = float(hdf5_getters.__getattribute__(getters[21])(h5,i))
                except AttributeError, e:
                    dance = None
                #print dance        

                try:
                    dur = hdf5_getters.__getattribute__(getters[22])(h5,i)
                except AttributeError, e:
                    dur = None
                #print dur        

                try:
                    eofi = hdf5_getters.__getattribute__(getters[23])(h5,i)
                except AttributeError, e:
                    eofi = None
                #print eofi    
            
                try:
                    ener = hdf5_getters.__getattribute__(getters[24])(h5,i)
                except AttributeError, e:
                    ener = None
                #print ener    
            
                try:
                    key = hdf5_getters.__getattribute__(getters[25])(h5,i)
                except AttributeError, e:
                    key = None
                #print key        

                try:
                    keyc = hdf5_getters.__getattribute__(getters[26])(h5,i)
                except AttributeError, e:
                    keyc = None
                #print keyc        

                try:
                    loud = hdf5_getters.__getattribute__(getters[27])(h5,i)
                except AttributeError, e:
                    loud = None
                #print loud        

                try:
                    mode = hdf5_getters.__getattribute__(getters[28])(h5,i)
                except AttributeError, e:
                    mode = None
                #print mode        
                
                try:
                    modec = hdf5_getters.__getattribute__(getters[29])(h5,i)
                except AttributeError, e:
                    modec = None
                #print modec
                
                try:
                    rel = hdf5_getters.__getattribute__(getters[30])(h5,i)
                except AttributeError, e:
                    rel = None
                #print rel
         
                try:
                    relsdid = int(hdf5_getters.__getattribute__(getters[31])(h5,i))
                except AttributeError, e:
                    relsdid = None
                #print relsdid        

                '''
                try:
                    secc = hdf5_getters.__getattribute__(getters[32])(h5,i)
                except AttributeError, e:
                    secc = None
                #print secc        

                try:
                    secs = hdf5_getters.__getattribute__(getters[33])(h5,i)
                except AttributeError, e:
                    secs = None
                #print secs

                try:
                    segc = hdf5_getters.__getattribute__(getters[34])(h5,i)
                except AttributeError, e:
                    segc = None
                #print segloudmax

                try:
                    segloudmax = hdf5_getters.__getattribute__(getters[35])(h5,i)
                except AttributeError, e:
                    segloudmax = None
                #print segloudmax        

                try:
                    segloudmaxtime = hdf5_getters.__getattribute__(getters[36])(h5,i)
                except AttributeError, e:
                    segloudmaxtime = None
                #print segloudmaxtime        

                try:
                    segloudstart = hdf5_getters.__getattribute__(getters[37])(h5,i)
                except AttributeError, e:
                    segloudstart = None
                #print segloudstart        

                try:
                    segpitches = hdf5_getters.__getattribute__(getters[38])(h5,i)
                except AttributeError, e:
                    segpitches = None
                #print segpitches        

                try:
                    segstart = hdf5_getters.__getattribute__(getters[39])(h5,i)
                except AttributeError, e:
                    segstart = None
                #print segstart        

                try:
                    segtimbre = hdf5_getters.__getattribute__(getters[40])(h5,i)
                except AttributeError, e:
                    segtimbre = None
                #print segtimbre    
            
                try:
                    simart = hdf5_getters.__getattribute__(getters[41])(h5,i)
                except AttributeError, e:
                    simart = None
                #print simart        

                '''

                try:
                    shot = float(hdf5_getters.__getattribute__(getters[42])(h5,i))
                except AttributeError, e:
                    shot = -1.0
                #print shot

                try:
                    songid = hdf5_getters.__getattribute__(getters[43])(h5,i)
                except AttributeError, e:
                    songid = None
                #print sofo        
                
                try:
                    sofo = hdf5_getters.__getattribute__(getters[44])(h5,i)
                except AttributeError, e:
                    sofo = None
                #print songid        

                '''
                try:
                    tatumsc = hdf5_getters.__getattribute__(getters[45])(h5,i)
                except AttributeError, e:
                    tatumsc = None
                #print tatumsc    
                
                try:
                    tatums = hdf5_getters.__getattribute__(getters[46])(h5,i)
                except AttributeError, e:
                    tatums = None
                #print tatums
                '''
                try:
                    tempo = hdf5_getters.__getattribute__(getters[47])(h5,i)
                except AttributeError, e:
                    tempo = -1.0
                #print tempo        

                try:
                    timesig = hdf5_getters.__getattribute__(getters[48])(h5,i)
                except AttributeError, e:
                    timesig = None
                #print timesig        

                try:
                    timesigc = hdf5_getters.__getattribute__(getters[49])(h5,i)
                except AttributeError, e:
                    timesigc = None
                #print timesigc    
            
                try:
                    title = hdf5_getters.__getattribute__(getters[50])(h5,i)
                except AttributeError, e:
                    title = None
                #print title        

                try:
                    tracksdid = hdf5_getters.__getattribute__(getters[51])(h5,i)
                except AttributeError, e:
                    tracksdid = None
                #print tracksdid        

                try:
                    trackid = hdf5_getters.__getattribute__(getters[52])(h5,i)
                except AttributeError, e:
                    trackid = None
                #print trackid        

                try:
                    year = hdf5_getters.__getattribute__(getters[53])(h5,i)
                except AttributeError, e:
                    year = None
                #print year
                
                '''
                print type(ambid)
                print type(aname)
                print type(apmeid)
                print type(amdfive)
                print type(dance)
                print type(dur)
                print type(eofi)
                print type(ener)
                print type(key)
                print type(keyc)
                print type(loud)
                print type(mode)
                print type(modec)
                print type(rel)
                print type(relsdid)
                print type(shot)
                print "sofo " + str(sofo)        
                print "songid " + str(songid)
                print tempo
                print timesig
                print timesigc
                print title
                print tracksdid
                print "track id " + str(trackid)
                print year
                '''

                '''
                "analysis_sample_rate" : self.analysis_sample_rate,
                "artist_7digitalid" : self.artist_7digitalid,
                "artist_familiarity" : self.artist_familiarity,
                "artist_hotttnesss" : self.artist_hotttnesss,
                "artist_id" : self.artist_id,
                "artist_latitude" : self.artist_latitude,
                "artist_location" : self.artist_location,
                "artist_longitude" : self.artist_longitude,
                "artist_mbid": self.artist_mbid,
                "artist_mbtags" : self.artist_mbtags,
                "artist_mbtags_count" : self.artist_mbtags_count,
                "artist_name": self.artist_name,
                "artist_playmeid": self.artist_playmeid,
                "artist_terms" : self.artist_terms,
                "artist_terms_freq" : self.artist_terms_freq,
                "artist_terms_weight" : self.artist_terms_weight,
                "artist_audio_md_five": self.artist_audio_md_five,
                "bars_confidence" : self.bars_confidence,
                "bars_start" : self.bars_start,
                "beats_confidence" : self.beats_confidence,
                "beats_start" : self.beats_start,
                
                "danceability": self.danceability,
                "duration": self.duration,
                "end_of_fade_in": self.end_of_fade_in,
                "energy": self.energy,
                "key": self.key,
                "key_confidence": self.key_confidence,
                "loudness": self.loudness,
                "mode": self.mode,
                "mode_confidence": self.mode_confidence,
                "release": self.release,
                "release_seven_digital_id": self.release_seven_digital_id,
                '''
                '''
                print type(secc)
                print type(secs)
                print type(segc)#self.segments_confidence,
                print type(segloudmax)
                print type(segloudmaxtime)
                print type(segloudstart)
                print type(segpitches)
                print type(segstart)
                print type(segtimbre)
                print type(simart)
                print type(tatumsc)
                print type(tatums)
                print type(atw)
                '''
                if year != None and year > 1998:
                    newSongData = songData(ambid,aname,apmeid,amdfive,dance,dur,eofi,ener,key,keyc,loud,mode,modec,rel,relsdid,shot,songid,sofo,tempo,timesig,timesigc,title,tracksdid,trackid,year)
                

                #newSongData = songData(asr,asdid,af,ah,aid,alat,aloc,alon,ambid,ambtag,ambtagc,aname,apmeid,at,atf,atw,amdfive,baconf,bastart,beconf,bestart,dance,dur,eofi,ener,key,keyc,loud,mode,modec,rel,relsdid,secc,secs,segc,segloudmax,segloudmaxtime,segloudstart,segpitches,segstart,segtimbre,simart,shot,songid,sofo,tatumsc,tatums,tempo,timesig,timesigc,title,tracksdid,trackid,year)
                    
                    masterList.append(newSongData)


            h5.close()
        json_string = json.dumps([ob.__dict__ for ob in masterList])
        with open('/Volumes/DUSTIN/OUT/' + letter + '.txt', 'w+') as fyle:
            fyle.write(json_string)
    
    

    print "Finished."
    print str(totalCount) + " Total"
    print str(len(masterList)) + " In List"

