# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.

def triangular(n):
    result = 1
    i = 2
    while i <= n:
        result += i 
        i += 1
    return result
        



print triangular(1)
#>>>1

print triangular(3)
#>>> 6

print triangular(10)
#>>> 55


#solution:
def triangular(n):
	number = 0
	for i in range(1, n + 1):
		number += i
	return number