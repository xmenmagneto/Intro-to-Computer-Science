# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    if list_of_numbers:
        biggest = 0
        for e in list_of_numbers:
            if e > biggest:
                biggest = e
        return biggest
    else:
        return 0



print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
#solution

def greatest(list_of_numbers):
	big = 0
	for i in p:
		if i > big:
			big = i
	return big