from numpy import*

arr1 = array([1,5,55,8,7])
arr2 = array([9,7,6,5,2])

for e in (arr1,arr2):
        arr = arr1+arr2

print(arr);

max = arr1[0];
for i in range(len(arr1)):
    if (arr1[i] > max):
        max = arr1[i]
print(max)