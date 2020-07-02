
class A():

       def __init__(self):
           print("In self")

       def feature1(self):
           print("feature 1 is workign")

       def feature2(self):
           print("feature 2 is workign")


class B():

    def feature3(self):
        print("feature 3 is workign")

    def feature4(self):
        print("feature 4 is workign")

class C(A,B):   #inheritance from Class A and Class B

    def feature5(self):
        print("feature 5 is workign")



a1 = A()
b1 = B()
c1 = C()

a1.feature1()
a1.feature2()
c1.feature1()

