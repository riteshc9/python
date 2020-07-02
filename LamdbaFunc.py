#lambda function and filter inbuild function
from functools import reduce

def is_even(n):
     return n%2==0

num = [1,2,3,4,5,6]

#filet function
result = list(filter(is_even, num))
print("Using normal filter function: ", result)


#filter and lambda function
num = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda n:n%2==0, num))
print("Using lambda function: ", result)

#Map function
m = list(map(lambda n:n*2,result))
print("using map function: ",m)

#Reduce function

sum = reduce(lambda a,b:a+b,m)
print("total: =",sum)
