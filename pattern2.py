#for i in range(5, 1,-1):                                   4 3 2 1
#    for j in range(i,1,-1):                                3 2 1
#        print(j-1, end = " ");                             2 1
#    print();                                               1

#for i in range(1, 5):                                  1
#    for j in range(1,i+1):                             1 2    
#        print(j, end = " ");                           1 2 3    
#    print();                                           1 2 3 4

for i in range (1,5):
    for j in range (i,5):
        print(j,end=" ")
    print()

a="ABCD"
b="PQR"
for i in range (4):
    for j in range (3):
        print(a[0:i+1],end=" ")      # A P Q R
        print(b[i:j+3],end=" ")      # A B Q R       
        break                        # A B C R   
    print()                          # A B C D  