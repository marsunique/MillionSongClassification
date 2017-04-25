from bs4 import BeautifulSoup
import os, os.path
import codecs

masterSongList = []
count = 0
for filename in os.listdir("data"):
    count = count + 1
    if count % 52 == 0:
        print filename
    path = os.path.join(os.getcwd(), "data", filename)

    with open(path, "r+") as newFile:
        htmlString = newFile.read()
        
        soup = BeautifulSoup(htmlString, 'html.parser')
    
        number = 1
        for link in soup.find_all('article'):
            artist = link.findAll(attrs={'class' : 'chart-row__artist'})
            
            if link.get('data-songtitle') is not None and not str(link.get('data-songtitle'))+"|~|"+artist[0].contents[0].strip()+ "\n" in masterSongList:
                masterSongList.append(str(link.get('data-songtitle')) + "|~|" + artist[0].contents[0].strip() + "\n")

duplicates = 0
print str(len(masterSongList))
masterSongList.sort()
print str(len(masterSongList))

length = len(masterSongList) - 1

for i in range(0,length):
    if masterSongList[i] == masterSongList[i+1]:
        duplicates = duplicates + 1

f = codecs.open('topSongs.txt', 'w', 'utf-8')
for song in masterSongList:
    print song
    f.write(song)
f.close()

print "duplicates: " + str(duplicates)
