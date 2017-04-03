#-*- coding: utf-8 -*-
import json
import csv
import codecs
import cStringIO
import os


# Might need this class UnicodeWriter in the future.
class UnicodeWriter(object):
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class JsonToCSV(object):
    def __init__(self, topsong_path):
        self.dir_path = "FAKE_PATH/data"
        self.file_list = os.listdir(self.dir_path)
        print self.file_list
        self.header = [
            'track_id', 'title', 'artist_name', 'release', 'year',
            'key', 'key_confidence', 'time_signature', 'time_signature_confidence', 'mode',
            'mode_confidence', 'end_of_fade_in', 'start_of_fade_out', 'energy', 'duration',
            'danceability', 'song_hottnesss', 'tempo', 'loudness', 'top100'
        ]
        topsong_file = open(topsong_path)
        try:
            self.topsong = topsong_file.readlines()
        except BaseException, e:
            print e
        finally:
            topsong_file.close()
    
    def readInput(self, input_path):
        json_file = open(input_path)
        try:
            data = json_file.read()
            json_data = json.loads(data)
            # json_data is a list of music data, each element contains attributes in json format
            # print json_data
            return json_data
        except BaseException:
            print 'Error when reading the ' + input_path
        finally:
            json_file.close()

    def stringIt(self, s):
        # print s
        # print type(s)
        if type(s) is unicode:
            return s.encode('utf-8')
        else:
            return str(s).encode('utf-8')

    def checkTop100(self, arg_title, arg_artist):
        for line in self.topsong:
            line = line.strip()
            title, artist = line.split('|~|')
            if title == arg_title and artist == arg_artist:
                return 'yes'.encode('utf-8')
        return 'no'.encode('utf-8')

    def transToCSV(self, json_data):
        result_list = []
        count_yes = 0
        count_no = 0
        try:
            for music in json_data:
                row = []
                for field in self.header[:-1]:
                    # print music[field]
                    value = self.stringIt(music[field])
                    # print type(value)
                    row.append(value)
                row.append(self.checkTop100(row[1], row[2]))
                row = tuple(row)
                # print row
                if row[-1] == 'yes':
                    count_yes += 1
                else:
                    count_no += 1
                result_list.append(row)
            print 'yes:', count_yes
            print 'no:', count_no
            return result_list
        except UnicodeDecodeError:
            print 'Encoding Error'

    def writeOutput(self, res, filename):
        output_file = open('millionSongs(labeled).csv', 'ab')
        try:
            writer = csv.writer(output_file)
            # if it is first .txt file, write header
            if filename == 'A.txt':
                writer.writerow(self.header)
            writer.writerows(res)
        except BaseException, e:
            print "Error when writing the 'tenksong.csv'"
            print e
        finally:
            output_file.close()

    def run(self):
        for filename in self.file_list:
            input_path = self.dir_path + '/' + filename
            print "Start converting " + filename
            json_data = self.readInput(input_path)
            res = self.transToCSV(json_data)
            print "Start creating .csv file..."
            self.writeOutput(res, filename)
            print filename + " Done!"



if __name__ == '__main__':
    test = JsonToCSV('topSongs.txt')
    test.run()
