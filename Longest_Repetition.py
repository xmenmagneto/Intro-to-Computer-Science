# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(list):
    if list:
        repetition = [[list[0], 1]]
        for i in range(1, len(list)):
            if list[i] == repetition[-1][0]:
                repetition[-1][1] += 1
            else:
                repetition.append([list[i], 1])
        longest = repetition[0]
        for i in range(1, len(repetition)):
            if repetition[i][1] > longest[1]:
                longest = repetition[i]
        return longest[0]
    else:
        return None




#For example,

#print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

#print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

#print longest_repetition([1,2,3,4,5])
# 1

#print longest_repetition([])
# None

print longest_repetition([2, 2, 2, 3, 3, 3, 3, 4, 4, 4])


#solution:

def longest_repetition(input_list):
    best_element = None
    length = 0
    current = None
    current_length = 0
    for element in input_list:
        if current != element:
            current = element
            current_length = 1
        else:
            current_length += 1
        if current_length > length:
            best_element = current
            length = current_length
    return best_element