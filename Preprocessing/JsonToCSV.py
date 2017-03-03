#-*- coding: utf-8 -*-
import json
import csv
import codecs
import cStringIO


# Might need this class UnicodeWriter in the future.
class UnicodeWriter:
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
    def __init__(self, filename):
        self.input_file = filename
        self.header = [
            'track_id', 'title', 'artist_name', 'release', 'year',
            'key', 'key_confidence', 'time_signature', 'time_signature_confidence', 'mode',
            'mode_confidence', 'end_of_fade_in', 'start_of_fade_out', 'energy', 'duration',
            'danceability', 'song_hottness', 'tempo', 'loudness'
        ]

    def stringIt(self, s):
        # print s
        # print type(s)
        if type(s) is unicode:
            return s.encode('utf-8')
        else:
            return str(s).encode('utf-8')

    def readInput(self):
        json_file = open(self.input_file)
        try:
            data = json_file.read()
            json_data = json.loads(data)
            # json_data is a list of music data, each element contains attributes in json format
            # print json_data
            return json_data
        except BaseException:
            print 'Error when reading the ' + self.filename
        finally:
            json_file.close()

    def transToCSV(self, json_data):
        result_list = []
        try:
            for music in json_data:
                row = []
                for field in self.header:
                    # print music[field]
                    value = self.stringIt(music[field])
                    # print type(value)
                    row.append(value)
                row = tuple(row)
                # print row
                result_list.append(row)
            return result_list
        except UnicodeDecodeError:
            print 'Encoding Error'

    def writeOutput(self, res):
        output_file = open('tenksongs.csv', 'wb')
        try:
            writer = csv.writer(output_file)
            writer.writerow(self.header)
            writer.writerows(res)
        except BaseException, e:
            print "Error when writing the 'tenksong.csv'"
            print e

    def run(self):
        json_data = self.readInput()
        res = self.transToCSV(json_data)
        print "Start creating .csv file..."
        self.writeOutput(res)
        print "Done!"



if __name__ == '__main__':
    test = JsonToCSV('tenksongs.txt')
    test.run()
    
    

        
        



