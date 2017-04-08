'''I really don'\t know what i'm doing '''
from math import pi
from time import sleep
from datetime import datetime
now = datetime.now()
print "Calculator starting up..."
print "Current time: %s/%s/%s %s:%s" %(now.month, now.day, now.year, now.hour, now.minute)
sleep(1)
hint = "Dont forget to include the correct units"
option = raw_input("Enter C for Circle or T for Triangle: ")
opttion = option.upper()
if option == "C":
  print "You entered C"
  radius = float(raw_input("Enter radius: "))
  area = pi * radius**2
  print("the pie is baking...")
  sleep(1)
  print ("Area: %.2f. \n%s" % (area, hint))
elif option == 'T':
  print "You entered T"
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = (0.5)*height * base
  print "Uni Bi Tri"
  sleep(1)
  print ("Area: %.2f. \n%s" % (area, hint))
else :
  print "Error! Invalid shape selector specified. Exiting."