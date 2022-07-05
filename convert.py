# converts the time we get from the page from a string to a float (that way we can graph the data)
def toNum(originalTime):
  if ((':' in originalTime) == False):
    return float(originalTime)
  else:
    timeParts = originalTime.split(":")
    min = float(timeParts[0])
    sec = float(timeParts[1])
    addSecs = min * 60
    totalTime = addSecs + sec
    return(totalTime)


# converts the float times back into strings (used for the x axis labels)
def toString(originalTime):
  if (originalTime < 60.0):
    return int(originalTime*10)/10
  else:
    min = int(int(originalTime)/60)
    sec = float(int((originalTime%60.0)*10))/10.0     #originalTime%60 gives the seconds—since we want to go to 2 digits, we multiply by 100, force it into an integer, then divide by 100
    if (sec<10):
      return f"{min}:0{sec}"
    else:
      return f"{min}:{sec}"