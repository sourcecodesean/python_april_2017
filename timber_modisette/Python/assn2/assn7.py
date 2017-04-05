'''sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']'''


value = "rubber baby buggy bumpers"

if type(value) is type(''):
	if len(value)<= 50:
		print "thats a short sentence."
	if len(value) > 51:
		print "thats a short sentence"

elif type(value) is type(0):
		if value >= 100:
			print "Thats a big number!"
		if value < 100:
			print "thats a small number"

elif type(value) is type([0,0]):
	if len(value) > 10:
		print "thats a long list"
	if len(value) < 10:
		print "thats a small list"
