def symm(a):
    n = len(a)
    flag = 0

    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2

    start1 = 0
    start2 = mid
    while start1 < mid and start2 < n:

        if a[start1] == a[start2]:
            start1 += 1
            start2 += 1
        else:
            flag = 1
            break

    if flag == 0:
        print("the string is symmetric")
    else:
        print("the string is not symmetric")


string = input("Enter your string")
symm(string)
