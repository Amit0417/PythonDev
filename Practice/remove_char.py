# # # removing the i'th character from the string. Method-1
# #
# # org_str = input("Enter your string")
# #
# # print("This is the original string = " + org_str)
# #
# # new_str = ""
# # n = int(input("enter the index of character you want to remove"))
# #
# # for i in range(len(org_str)):
# #     if i != n:
# #         new_str = new_str + org_str[i]
# #
# # print("String after removing the i'th character = " + new_str)
#
# #removing the i'th character from the string using str.replace. Method 2
#
# org_str1 = input("Enter your string")
# print("This is the original string = " + org_str1)
# n = input("Enter the charater you want to remove")
# new_str1 = org_str1.replace(n,"",1)
# print(new_str1)
#
