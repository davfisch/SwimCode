from bs4 import BeautifulSoup # used to parse html pages
import requests # used to retrieve html pages
import numpy as np # helps with graphing data
from Datapoint import Datapoint
import convert
from ClubStats import ClubStats

class EventStats:
    
    def __init__(self, link):
        self.link = link
        self.loadData()

    def loadData(self):
        r = requests.get('https://www.swimmingrank.com/ne/ne/scy_boys_17_18_50FR_current.html') #retreive the html of the page (this has the data we need)
        soup = BeautifulSoup(r.content, 'html.parser') #turn the html into an object that we can parse
        list = soup.html.find_all('tr') #create an array of all the <tr> tags (this is where we'll find the times that we want)

        #remove the first and last elements of the array (they're other things that we don't want, the remaining elements will be the times we need)
        list.pop(0)
        list.pop()

        infoList = [] # hold all data on each swimmer

        #add all the times (as ints) to a list
        for tr in list: # 0: rank, 1: name, 2: age, 3: club name, 4: time, 5: date, 6: meet name
            data = tr.find_all("td")
            rank = data[0].text.strip()
            name = data[1].text.strip()
            age = data[2].text.strip()
            club = data[3].text.strip()
            time = data[4].text.strip()
            date = data[5].text.strip()
            meet = data[6].text.strip()
            dataPoint = Datapoint(rank, name, age, club, time, date, meet)
            infoList.append(dataPoint)

            stats = ClubStats()

        for i in infoList:
            stats.addTime(i)

        self.stats = stats

        # save the name of the event
        self.eventName = soup.html.find("h2").text.split("Short")[0].strip()

    def getRankings(self):
        sortedArray = self.stats.summaryStats() # get club names and averages
        str = f"{self.eventName} Rankings\n"

        # make rankings look nice
        for i in range(len(sortedArray)):
            club = sortedArray[i][0]
            avg = sortedArray[i][1]
            str += f"{i+1}. {club}: {avg}"
            if (i != len(sortedArray)-1):
                str += "\n"
        return str
