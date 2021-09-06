# Python3 code to demonstrate working of
# Avoid Spaces in Characters Frequency
# Using isspace() + sum()

# initializing string
test_str = 'geeksforgeeks 33 is   best'

# printing original string
print("The original string is : " + str(test_str))

# isspace() checks for space
# sum checks count
res = int(sum(not chr.isspace() for chr in test_str))

# printing result
print("The Characters Frequency avoiding spaces : " + str(res))