# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    i = 1
    factorial = 1
    while i <= n:
        factorial = factorial * i
        i = i + 1
    return factorial



print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
print factorial(6)
#>>> 720





#alternative solution
def factorial(n):
	result = 1
	while n >=1:
		result = result * n
		n = n - 1
	return result