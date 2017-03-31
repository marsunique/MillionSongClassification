#-*- coding: utf-8 -*-
import csv

class Hotness(object):
    def __init__(self, topsong_path):
        topsong_file = open(topsong_path)
        try:
            self.topsong = topsong_file.readlines()
        except BaseException, e:
            print e
        finally:
            topsong_file.close()
    
    def writefile(self, dic):
        output_file = open('topartist.csv', 'wb')
        try:
            writer = csv.writer(output_file)
            writer.writerows(dic)
        except BaseException, e:
            print "Error when writing the 'tenksong.csv'"
            print e
        finally:
            output_file.close()
    
    def run(self):
        dic = {}
        for line in self.topsong:
            line = line.strip()
            artist = line.split('|~|')[1]
            dic.setdefault(artist, 0)
            dic[artist] += 1
        # sort dic by count of artist
        dic = sorted(dic.items(), key=lambda d:d[1], reverse=True)
        print dic
        self.writefile(dic)

if __name__ == '__main__':
    test = Hotness('topSongs.txt')
    test.run()