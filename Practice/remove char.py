# removing the i'th character from the string.

org_str = input("Enter your string")

print("This is the original string " + org_str)

new_str = ""
n = int(input("enter the index of character you want to remove"))

for i in range(len(org_str)):
    if i != n:
        new_str = new_str + org_str[i]

print("String after removing the i'th character " + new_str)
