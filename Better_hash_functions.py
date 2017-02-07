# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    sum_of_ord = 0
    for e in keyword:
        sum_of_ord +=ord(e)
    hash = sum_of_ord % buckets
    return hash





print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11


#solution: 以下方法更好，当h很长时， 求模运算很耗内存
def hash_string(keyword, buckets):
	h = 0
	for c in keyword:
		h = (h + ord(c)) % buckets
	return h