def add_time(start, duration, weekDay = "Nothing"):

  dayInfo = ""

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

  #try:
   # mins = int(startTimeMins) + int(durationMins)
    #hours = int(startTimeHours) + int(durationHours)
  #except:
  #  print("Time and duration should contain time format.")

  startTimeHours = int(startTimeHours)
  durationHours = int(durationHours)

  #change to 24hr format 
  if am_pm_start == "PM":
    startTimeHours += 12
  # 

  [c, r] = divmod(durationHours,24)
  if c > 0:
    #agrego c dias
    print(c)
  #
  totalHours = startTimeHours + r   #r = remaining hours

  if totalHours > 24:
    #agrego 1 dia
    totalHours -= 12 
    print(totalHours)
  #

  totalHours -= 12    #final hours
  am_pm = am_pm_start 
  if totalHours > 12:
    if am_pm_start == "PM":
      am_pm = "AM"
    else:  
      am_pm = "AM"
  #


  mins = 0
  dayInfo = ""
  new_time = str(totalHours)+":"+str(mins).zfill(2)+" "+am_pm+dayInfo


  ##################### IGNORE BELOW  ####################

  mins = 0
  hours = 0
  if mins >= 60:  #add 1hr if time reaches 60 minutes
    mins -= 60
    hours += 1
  #


  #change to 24hr format and add totals
  if am_pm_start == "PM":
    hours = int(startTimeHours) + 12 + int(durationHours) #1PM = 13hs 
  else:
    hours = int(startTimeHours) + int(durationHours)
  #
  mins = int(startTimeMins) + int(durationMins)
  if mins >= 60:  #add 1hr if time reaches 60 minutes
    mins -= 60
    hours += 1
  #


  #c = how many days, r = how many extra hours -> 51/24 => c = 2, r = 3. 2 days, 3 hours
  [c, r] = divmod(hours,24) 
  if c == 1:
    dayInfo = " (next day)"
  elif c > 0:
    dayInfo = " ("+c+" days later)"


  #ver cuando r es mayor a 24hs tengo que volver a sumar dias 




  
  return new_time


  # a // b -> floor division. Rounds the result down to the nearest whole number
