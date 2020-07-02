# There are 3 typr of class methods
#instance method, class method and static method

class student:

    clg = "IIT-B"

    def __init__(self, m1, m2 ,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

     #Instance method
    def avg(self):
         return ((self.m1+self.m2+self.m3)/3)

     #class methond
    @classmethod
    def getcollege(cls):
         return cls.clg

     #static method
    @staticmethod
    def info():
         print("This is static method class")


s1 = student(5,10,15)
s2 = student(10,20,30)

print(s1.avg())
print(s2.avg())

print(student.getcollege())
print(student.getcollege())

student.info()
student.info()