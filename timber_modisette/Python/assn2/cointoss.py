import random
'''def coin_toss():

	heads_count=0
	tails_count=0
	attempts=0
	result =""

	for x in range(1,21):
		#print x
		new_flip = random.randint(0,1)
		#print new_flip
		if new_flip == 1:
			heads_count = heads_count +1
			#print heads_count
			attempts = attempts+1
			result= "heads"
			print "Attempt #",attempts," Throwing a coin it's a ",result,". Got ",heads_count ,"head(s) so far and", tails_count, "tail(s) so far"
		if new_flip == 0:
			tails_count = tails_count+1
			attempts = attempts +1
			result = "tails"
			print "Attempt #",attempts," Throwing a coin it's a ",result,". Got ",heads_count ,"head(s) so far and", tails_count, "tail(s) so far"
			

coin_toss()'''

heads_count = 0
tails_count = 0
for x in range(1,21):
	new_flip = random.randint(0,1)
	if new_flip == 0:
		heads_count = heads_count +1
		print "Attempt #{}. Throwing a coin, it's a heads. Got {} head(s) and {} tail(s)".format(x,heads_count,tails_count)
	else:
		tails_count = tails_count +1
		print "Attempt #{}. Throwing a coin, it's a tails. Got {} tail(s) and {} head(s)".format(x,tails_count,heads_count)
