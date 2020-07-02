from array import *


# enter array from user
arr = array('i',[])
n = int(input("Enter the length of array"))

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)

print(arr)

val =int(input("Enter the value for search"))
k=0
for j in arr:
    if j==val:
        print("value found and index number =",k)
        break

    k = k+1

"""
# print array and add value 

num = array('i', [1, 2, 3, 4])
num.append(6)
print(num)

for i in range(5):
    print(num[i],end="  ")
print()
for i in num:
    print(i)
    
"""


