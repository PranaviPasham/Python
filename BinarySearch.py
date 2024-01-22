pos = -1
i = 0
searchlist=[]
def search(searchlist,n):
    l = 0
    u = len(searchlist) - 1
    for i in range(len(searchlist)):
        mid = (l+u) // 2
        if searchlist[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if searchlist[mid] < n:
                l= mid + 1
            else:
                u = mid - 1
    return False

#searchlist = [3,6,8,1,9]
n = int(input("Enter the length of list : "))
x = input("Enter the list with comma seaprated values:")
for i in range(n):
    #x = int(input("Enter the list :"))
    searchlist = x.split(',')
    searchlist = [int(value) for value in searchlist]
print(searchlist)
n = int(input("Enter the number for search : "))

if search(searchlist,n):
    print("Found the number",pos+1)
else:
    print("Not found")