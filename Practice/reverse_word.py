# reverse the word  in the given string without using function
string = "geeks quiz practice code"
s1 = string.split()
s2 = s1[::-1]
out = " ".join(s2)
print(out)


# reverse the word in given string using function
def rev(string_1):
    words = string_1.split(' ')
    rev_string = " ".join(reversed(words))
    stringx = dddrev_string[:-1]+rev_string[:-1].upper()
    return stringx


# if __name__ == "__main__":
str1 = "geeks quiz practice code"
str2 = input("enter your string")
print(rev(str1))
print(rev(str2))
