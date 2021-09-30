# bubble short
def b_short(lst_1 ):
    count = 0
    for _it_ in range(len(lst_1) - 1, 0, -1):
        for _ind_ in range(_it_):
            if lst_1[_ind_] > lst_1[_ind_ + 1]:
                bubble = lst_1[_ind_]
                lst_1[_ind_] = lst_1[_ind_ + 1]
                lst_1[_ind_ + 1] = bubble

        # for iteration counts
        count += 1
        print("After completed parse ", count, "=>", lst_1)
    print("number of iteration = ", count)


list_1 = []
print("enter the number of element")
n = int(input())
for i in range(n):
    print("enter element")
    x = int(input())
    list_1.append(x)

print("list before short ", list_1)
b_short(list_1)
print("list after short ", list_1)
