#Aleena Naeem - Assignment 1A

#Part 1a
#input
distance=float(input('Enter distance(miles) greater that 0:'))
speed=float(input('Enter speed greater than 0(miles/hour):'))


#processing
timeHour = speed/distance

#output
print('Time the route should take (in hours) is', round(timeHour,2))

#Part 1b
#input
distance=float(input('Enter distance(miles):'))
speed=float(input('Enter speed(miles/hour):'))

#processing
timeMinutes = (speed/distance)*60

#output
print('Time the route should take (in minutes) is', round(timeMinutes))

#Part 3
#input
localdistance=30
localspeed=30
parkwaydistance=35
parkwayspeed=40
highwaydistance=48
highwayspeed=55

#processing

localtime=float(localspeed/localdistance)
parkwaytime=float(parkwayspeed/parkwaydistance)
highwaytime=float(highwayspeed/highwaydistance)

#output
print('local time in hours is=',(round(localtime,2)))
print('parkway time in hours is=',(round(parkwaytime,2)))
print('highway time in hours is=', (round(highwaytime,2)))
