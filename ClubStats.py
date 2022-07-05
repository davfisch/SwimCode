import convert
import statistics

class ClubStats:
    clubsDict = {}
    # {"club": [time1, time2, time3, ...]}
    def addTime(self, datapoint):
        if (datapoint.club not in self.clubsDict):
            self.clubsDict[datapoint.club] = [convert.toNum(datapoint.time)]
        else:
            self.clubsDict[datapoint.club].append(convert.toNum(datapoint.time))

    def average(self, club):
        if club in self.clubsDict:
            return statistics.mean(self.clubsDict[club])
    
    def median(self, club):
        if club in self.clubsDict:
            return statistics.median(self.clubsDict[club])

    def summaryStats(self):
        # make array of sorted average times
        averagesDict = {}
        for key in self.clubsDict:
            averagesDict[key] = self.average(key)
        sortedArray = sorted(averagesDict.items(), key = lambda item:item[1])
        return(sortedArray)