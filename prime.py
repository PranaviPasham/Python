import math

i = int(input("Enter a number : "))
#if i == 2:
#    print("Prime Number",i)
#elif i%2 != 0:22
#    print("Prime Number", i)
#else:
#    print("Not a Prime Number",i)
temp = 1;
for x in range(2,int(math.sqrt(i)),1):
    if i%x == 0:
        temp = 0;
        break;
if temp == 0:
    print("Not Prime",i)
else:
    print("Prime",i)