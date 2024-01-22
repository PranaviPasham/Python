pos = -1
i = 0
def search(searchlist,n):
    for i in range(len(searchlist)):
        if searchlist[i] == n:
            globals()['pos'] = i
            return True
    return False

#searchlist = [3,6,8,1,9]
n = int(input("Enter the length of list : "))
searchlist=[]
x = input("Enter the list with comma seaprated values:")
for i in range(n):
    #x = int(input("Enter the list :"))
    searchlist = x.split(',')
    searchlist = [int(value) for value in searchlist]
print(searchlist);
n = int(input("Enter the number for search : "))

if search(searchlist,n):
    print("Found the number",pos+1)
else:
    print("Not found")