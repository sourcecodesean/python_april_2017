
def odds_evens():
	for x in range(1,2001):
		if x % 2 == 0:
			print "the number is ", x, ".This is an even number."
		else:
			print "the number is ", x, ".This is an odd number."



odds_evens()


def multiply(a,num):
	newList = []
	for x in a:
		 newList.append(x * num)
	return newList 





a = [1,2,3,4,5]

b = multiply(a,5)
#print b



def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

#b =multiply([2,4,5],3)

#x = layered_multiples(b)
#print x
