
n = int(input("Enter a number for factorial :"))

def fact(n):
    f =1;
    for i in range(1,n+1):
        f = f * i
    return f;
res = fact(n)
print(res)