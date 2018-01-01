animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print animals

for i in animals:
	print i
	
	
print ""
print "First, second, third are ordinal numbers, but we"
print "need to count by cardinal numbers: 1, 2, 3,"
print "With lists, you start at 0."
print ""

for i in range(len(animals)):
	print "Index %d in the list is %s." % (i, animals[i])
	
	