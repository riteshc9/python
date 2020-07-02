
#Define Fibonacchi number fucntion
def fibo(n):
   a = 0
   b = 1
   list = []
   if n ==1:
        print(a)
        list = [a]
   else:
        print(a)
        print(b)
        list = [a , b]
        for i in range(2 ,n):
             c = a+b
             a = b
             b = c
             print(c)
             list.append(c)

   return list

#Find out number from the list and ask from user which number they want
# find out number greater than 30 and less than 40 in first 10 fibonacci number

def findnumber(list):


n = int(input("Pibonacci number till: "))

list = fibo(n)
print("Fibonacci number list: ",list)

Number = findnumber(list)
print(Number)