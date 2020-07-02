#Overrding
class A:

    def show(self):
        print("In A show")

class B(A):
    # first we dont have this then answer was "In A show" but when we show in B we dont print "In A show"
    # this called overriding
    def show(self):
        print("In B show")

s1 = B()
s1.show()


# #Overloading
# class student:
#
#     def __init__(self):
#         print("init")
#
# #Overloading of None to user defined value
#     def sum(self,a=None ,b=None):
#
#         if a!=None and b!=None:
#            s = a+b
#         else:
#            s =a
#
#         return s
#
#
# s1 = student()
#
# print(s1.sum(4,5))
