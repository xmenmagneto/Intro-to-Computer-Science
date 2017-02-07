# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159


#ENTER CODE BELOW HERE

#get original string
s = str(x)

#get decimal position
decimalPosition = s.find(".")

#get the str(the 1st digit after decimal)
stringAfterDecimal = s[decimalPosition+1:decimalPosition+2]

#check if the string contains 5-9, if so increase x by 1

x += stringAfterDecimal.find('5')+1
x += stringAfterDecimal.find('6')+1
x += stringAfterDecimal.find('7')+1
x += stringAfterDecimal.find('8')+1
x += stringAfterDecimal.find('9')+1



#get new string of rounded x
newString = str(x)


#find the new position of decimal
newDecimalPosition = newString.find(".")

#truncate x to be integer
truncateString = newString[0:newDecimalPosition]


print truncateString 




#improvements

给每个数字加0.5即可进位












