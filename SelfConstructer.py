class computer:

    def __init__(self):
        self.name = "ritesh"
        self.age = 30

    def Name(self):
        print("Name & age", self.name , self.age )

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
           return False

c1 = computer()
c1.age = 29
c2 = computer()

if c1.compare(c2):
    print("Same age")
else:
    print("Not same")

