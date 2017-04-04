list = ['hello','world','my','name','is','Anna','world']
char = 'o'


newList = []



for x in range(0,len(list)):
	if list[x].find("o") > 0:
		newList.append(list[x])


print newList




