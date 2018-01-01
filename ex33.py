i = 0
numbers = []

while i < 6:
	print "At the top i is: %d" % i
	numbers.append(i)
	i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	


print "The numbers: "

for num in numbers:
	print num
	

# Going over the study drills

print "\nConverting the while-loop to function, drill_1"

def drill_1(n):
	i = 0
	numbers1 = []
	while i < n:
		print "Item: %d" % i
		numbers1.append(i)
		i += 1
	print numbers1
	
	
	
print "\nUsing drill_1 with n = 3"
drill_1(3)

print "\nUsing drill_1 with n = 8"
drill_1(8)


print "\nCreating function drill_3 to allow variable step size"

def drill_3(n, step):
	i = 0
	numbers3 = []
	while i < n:
		print "item: %d" % i
		numbers3.append(i)
		i += step
	print numbers3
	

print "\nUsing drill_3 with n = 12 and step = 3"
drill_3(12, 3)



print "\ndrill_5 uses a for loop and range instead"

def drill_5(n, step):
	numbers5 = range(0, n, step)
	for i in numbers5:
		print "Item: %d" % i
	print numbers5
	
	
drill_5(14, 4)














