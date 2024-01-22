import array as arr

ar = arr.array('i',[])
 
n = int(input("Enter the length of array : "))

for i in range(n):
    x = int(input("Enter next value : "))
    ar.append(x)

print("Deleting value at index 2 without inbuilt function")

ar.pop(2)

print(ar)
    
