n = int(input("Enter the length of list : "))
lst=[]
for i in range(n):
    x = input("Enter  Names :")
    lst.append(x);
print(lst);


def StringCount(lst):
    greater = 0;
    lesser = 0;
    for i in lst:
        if len(i) >=5:
            greater += 1;
        else:
            lesser += 1;
    return greater,lesser

greater,lesser = StringCount(lst)

print("Names greater than 5 {}, Names lesser than 5 {}".format(greater,lesser))