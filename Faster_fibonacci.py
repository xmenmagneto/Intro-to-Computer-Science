#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        previous_two = 0
        previous_one = 1
        i =2
        while i <= n:
            present = previous_two + previous_one
            previous_two = previous_one
            previous_one = present
            i += 1
        return present
    





print fibonacci(36)
#>>> 14930352



#solution:
def fabonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        #multiple assignment, no need for temp
        current, after = after, current + after
    return current