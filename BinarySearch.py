
#Search element in the list with binary search
pos =-1
def find(list, n):

     l =0  # lower bound
     u = len(list)-1    #upper bound

     while l<= u:
         m = (l+u)//2  # // will give us int value  so m will be int
         if list[m]==n:
             globals()['pos'] = m
             return True
         else:
             if list[m] < n:
                 l = m+1
             else:
                 u = m-1
     return False

list = [1, 2, 3, 4, 5]

n = int(input("Enter the element which you want to serach in list:  "))

if find(list , n ):
    print("found at: ",pos)
else:
    print("not found")