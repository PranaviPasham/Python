print("While Loop")
x = 1;
while x in range(2,5):
    first = 0;
    second = 1;
    print(first, end = " ")
    print(second, end = " ")
    x = first + second;
    first = second;
    second = x;
    print(x, end = " ");

print()
print()

n = int(input("Enter number for fibnocii : "))
print("For Loop")
def fib(n):
    a = 0;
    b = 1;
    if n<0:
        print("Enter a  positive number")
    elif n==1:
        print(a, end = " ")
    else:
        print(a, end = " ")
        print(b, end = " ")
        for i in range(2,n):
            c = a+b
            a=b
            b = c
            if c>n:
                break
            print(c, end = " ")
fib(n)