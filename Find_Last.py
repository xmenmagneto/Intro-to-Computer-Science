# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.


#get the position of next target
def get_next_target(search,target,start):
    start_position = search.find(target,start)
    if start_position == -1:
        return -1
    return start_position



def find_last(search,target):
    result = -1  #initialize the poition result
    start = 0
    while True:
        start = get_next_target(search,target,start)
        if start != -1:
                result = start
                start = start + 1   #update the start position
        else:
            break
    return result
    



#improvements
def find_last(s,t):
    last = -1  #last position
    while True:
        pos = s.find(t, last + 1)
        if pos == -1: #did not find new position
            return last
        last = pos







print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0


