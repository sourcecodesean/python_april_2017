x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
print x


print (len(x)/2)

print (x[:len(x)/2])
print (x[len(x)/2:])

first = (x[:len(x)/2])
second = (x[len(x)/2:])

y = []

y.append(first)
y.append(second)

print y