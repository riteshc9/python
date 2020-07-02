# count number of even number and odd number from list

# define function for even and odd

def even_odd(list):
    even = 0
    odd = 0

    for i in list:
         if i%2==0:
             even+=1
         else:
             odd+=1

    return even, odd
# Creating an empty list
list = []

#number of element as input
n = int(input("Enter the number of element :  "))

#take list element form user and add it
for i in range(0,n):
    ele = int(input("enter element : "))
    list.append(ele)
print(list)

even, odd = even_odd(list)

print("Number of even number in list : ",even)
print("Number of odd number in list : ",odd)

print("even : {} and odd : {} ".format(even,odd))
