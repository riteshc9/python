print("*****************Hello Lockdown 4.0*******************")
print("************Welcome to Python learning************")

# find the prime number
num = 4
for i in range(2,num):
    if num % i == 0:
        print("Not prime number")
        break
else:
    print("prime")


#***************For and else**********************
# found number divisible by 5
"""
num = [3, 6, 15, 20, 22, 30, 35]

for i in num:
    if i % 5 == 0:
        print(i)
    else:
        print(i, "= Number not divisible by 5")
"""
#***************Print pattern**********************
""""
for j in range(4):
    for i in range(4-j):
        print("*", end="")

    print()
"""

