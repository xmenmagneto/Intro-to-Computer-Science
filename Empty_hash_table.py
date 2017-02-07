# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    i = 1
    hash_table = [[]]
    while i < nbuckets:
        hash_table.append([])
        i += 1
    return hash_table
        

print make_hashtable(5)


#solution 1

def make_hashtable(nbuckets):
	i = 0
	table = []
	while i < nbuckets:
		table.append([])
		i += 1
	return table



#solution 2
# built-in metho:   range(<start>, <stop>)
#output: [<start>, <start> + 1, ... , <stop> - 1]
#range(0 ,10) -> [0, 1, 2, ... ,9]

def make_hashtable(nbuckets):
	table = []
	for unused in range(0 , nbuckets):
		table.append([])
	return table