def draw_stars(x):
	for i in range(0,len(x)):
		for j in range(x[i]):
			print "*",
		print('\n')






x = [4, 6, 1, 3, 5, 7, 25]
#draw_stars(x)





def draw_stars(arr):
	for i in range(0,len(arr)):
		if type(arr[i]) == type(0):
			for j in range(arr[i]):
				print "*",
			print('\n')
		if type(arr[i]) == type("s"):
			for k in range(0,len(arr[i])):
				print arr[i][0],
			print "\n"


arr = ['tim', 6, 1, 3, 5, 7, 25]
#draw_stars(arr)





def draw_stars(list):
	for value in list:
		print '*' * value

#draw_stars([2,3,4,5])


def draw_stars(list):
	for item in list:
		if type(item) is int:
			print "*" * item
		elif type(item) is str:
			print str(item[0].upper()) * len(item)

draw_stars([2, "tom", 1, "piff"])


