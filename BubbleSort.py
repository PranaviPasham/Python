sortlist = []
list = input("Enter the list values with comma separation : ")
for lst in range(len(list)):
    sortlist = list.split(',')
    sortlist = [int(value) for value in sortlist]
#print(sortlist)

def bubblesort(sortlist):
    for i in range(len(sortlist)-1,0,-1):
        for j in range(i):
            if sortlist[j] > sortlist[j+1]:
                temp = sortlist[j]
                sortlist[j] = sortlist[j+1]
                sortlist[j+1] = temp

bubblesort(sortlist)

print(sortlist)