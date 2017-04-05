import random

def scores_grades():
	arr = []
	for i in range(0,10):
		arr.append(random.randint(60,100))
	print arr

	for x in arr:
		if x >= 90:
			print "score: ", x,"; your grade is an a"
		if x >= 80 and x <=89:
			print "score: ", x,"; your grade is a b"
		if x >= 70 and x <=79:
			print "score: ", x,"; your grade is a c"
		if x >=60 and x <=69:
			print "score: ", x,"; your grade is a d"
	print "end of program goodbye"





scores_grades()