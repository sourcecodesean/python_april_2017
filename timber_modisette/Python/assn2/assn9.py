list1 = [1,1,1,1,1]
list2 = [1,1,1,1,1]
		
count = 0
		




'''if cmp(list1, list2) == 0:
	print "The lists are identical"

else:
	print "they are different"'''


if len(list1) == len(list2):

	for x in range(0, len(list1)):
			
		if  list1[x] == list2[x]:
			count = count + 1
			
		else:
			print "not the same"

	if count == len(list1) and count == len(list2):
		print "they are the same"
elif len(list1) != len(list2):
	print "not the same"