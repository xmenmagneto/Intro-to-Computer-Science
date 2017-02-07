# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

#using while loop
def find_element(list, value):
    check = -1
    i = 0
    while i < len(list):
        if list[i] == value:
            check = i
            return check
        i += 1
    return check


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1


#using built in method
def find_element(p, t):
    if t in p:
        return p.index(t)
    else:
        return -1




print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1





#solution1
def find_element(p, t):
	i = 0
	while i < len(p):
		if p[i] == t:
			return i
		i = i + 1
	return -1

#solution 2 
def find_element(p ,t):
	i = 0
	for e in p:
		if e == t:
			return i
		i = i + 1
	return -1


#built in method


# 1.   <list>.index(<value>)
		#不同之处：若找不到，则返回error，而非-1


# 2.   <value> in <List> 
		#输出True / False

# 3.   <value> not in <List> 
		#输出True / False
		#<value> not in <List>  全等于 not <value> in <list>

#solution 3
def find_element(p, t):
	if t not in p:
		return -1
	return p.index(t)

