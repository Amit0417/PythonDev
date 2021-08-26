def pal(a):
    mid = (len(a) - 1) // 2
    start = 0
    last = len(a) - 1
    flag = 0

    while (start <= mid):
        if (a[start] == a[last]):
            start +=1
            last -=1
        else:
            flag = 1
            break;

    if(flag==0):
        print("The enterd sting is palindrome")
    else:
        print("The entered sting is not palindrome")

string=input("enter your string")
pal(string)
