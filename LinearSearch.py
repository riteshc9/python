
#Search element in the list




pos = -1
def find(list, n):
     # i = 0
     # while i < len(list):
     #     if list[i]==n:
     #         return True
     #     i = i+1
     # return False

     for i in list:
       if i==n:
          globals()['pos'] = i
          return True

list = [1, 2, 3, 4, 5]
n = int(input("Enter the element which you want to serach in list:  "))

if find(list , n ):
    print("found at: ",pos)
else:
    print("not found")