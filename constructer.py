
class A():

       def __init__(self):
           print("In A class")

       def feature1(self):
           print("feature 1 is workign")

       def feature2(self):
           print("feature 2 is workign")


class B(A):

    def __init__(self):
        super().__init__()              # this is use to call parent init as well
        print("In B class")

    def feature3(self):
        print("feature 3 is workign")

    def feature4(self):
        print("feature 4 is workign")

    def call(self):
        super().feature1()



a1 = B()
a1.call()

