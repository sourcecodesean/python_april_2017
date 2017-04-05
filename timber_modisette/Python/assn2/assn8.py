list = ["piff","piff"]

sum = 0
str = ""


for value in list:
	if type(value) == type(0) or type(value) == type(1.99):
		sum = sum + value


	elif type(value) == type(""):
		str = str + " " + value

if sum!= 0 and len(str)!= 0:
	print "this is a mixed list"
	print "sum: "
	print sum
	print "str: "+str

if sum!= 0 and len(str) == 0:
	print "this is an interger list"
	print "sum: "
	print sum

if sum == 0 and len(str)!= 0:
	print "this is a string list"
	print "str: "+str

