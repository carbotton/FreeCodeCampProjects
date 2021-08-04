def add_time(start, duration, weekDay = None):

  try:
      [startTime, am_pm_start] = start.split(" ")
  except:
      print("Missing information in start time.")
  
  try:
    [startTimeHours, startTimeMins] = startTime.split(":")
  except:
    print("Missing information in start time.")

  try:
    [durationHours, durationMins] = duration.split(":")
  except:
    print("Missing information in duration.")

  try:
    startTimeHours = int(startTimeHours)
    durationHours = int(durationHours)
    startTimeMins = int(startTimeMins)
    durationMins = int(durationMins)
  except:
    print("Time and duration should contain time format.")

  #init
  totalHours = 0
  weekDaysDict = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6} 
  if weekDay:
    dayInfo = ", "+weekDay
  else:
    dayInfo = "" 
  #

  #change to 24hr format 
  if am_pm_start == "PM":
    startTimeHours += 12
  # 

  #handle minutes
  totalMins = startTimeMins + durationMins

  if totalMins >= 60:  #add hours
    [c, r] = divmod(totalMins, 60)
    if c > 0:  #add c1 hours
      totalHours = c
    if r > 0:
      totalMins = r
  #  

  #handle hours
  [daysToAdd, hoursToAdd] = divmod(durationHours, 24)

  totalHours += startTimeHours + hoursToAdd   #hoursToAdd = remaining hours

  if totalHours >= 24:   #add 1 day
    daysToAdd += 1
    totalHours -= 24  
  #

  #handle am - pm
  am_pm = "AM" 
 
  if totalHours >= 12:
    am_pm = "PM"
    totalHours -= 12    #final hours
  #     

  if totalHours == 0:
    totalHours = 12
  #

  if daysToAdd > 0: 

    if weekDay:
      weekDay = weekDaysDict[weekDay.lower()]
      [weeks, days] = divmod(weekDay, 7)
      weekDay += days
      [temp, finalWeekDay] = divmod(weekDay, 7)
      dayInfo = list(weekDaysDict.keys())[list(weekDaysDict.values()).index(finalWeekDay)]
      dayInfo = list(dayInfo)
      dayInfo[0] = dayInfo[0].upper()
      dayInfo = ", " + str("".join(dayInfo))

    else:
      if daysToAdd == 1:
        dayInfo = " (next day)"
      else:
        dayInfo = " (" + str(daysToAdd) + " days later)"
      #
  #

  new_time = str(totalHours)+":"+str(totalMins).zfill(2)+" "+am_pm+dayInfo

  return new_time
