from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta
import os


# READ THE FILES FROM BILLBOARD.
# THIS METHOD WILL READ EVERY BILLBOARD TOP 100 LIST AND PRINT THE RESULT
# INTO THE data/ FOLDER.  IF THERE IS NO DATA FOLDER, IT WON'T WORK, JUST FYI






date = datetime.date(2000,1,1)


#print "" + str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "-" + str(date.weekday())

while True: #not (date.year != 2017 and date.month != 3 and date.day != 25):
    if date.year == 2017 and date.month > 3:
        break

    #date < datetime.datetime.now():
    #date.year < datetime.datetime.now().year or date.month < datetime.datetime.now().month or date.day < datetime.datetime.now().day:
    #print "" + str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "-" + str(date.weekday())

    # we need to do leading zeroes
    month = str(date.month)
    if date.month < 10:
        month = "0" + str(date.month)
    
    day = str(date.day)
    if date.day < 10:
        day = "0" + str(date.day)
    
    dateString = str(date.year) + "-" + month + "-" + day
    print dateString
    
    #yolo = urlopen("http://www.billboard.com/charts/hot-100/2017-03-25").read()
    yolo = urlopen("http://www.billboard.com/charts/hot-100/" + dateString).read()


    with open("data/" + dateString + ".txt", "w") as outFile:
        outFile.write(yolo)




    ''' -> Use to print the data that you're writing
    soup = BeautifulSoup(yolo, 'html.parser')

    #print(soup.prettify())
    soup.find_all('article')

    for link in soup.find_all('article'):
        print(link.get('data-songtitle'))
    '''
    date = date + timedelta(days=7)

    #print yolo
    
