# Define class
class car:

    company = "Mercedes"    # Class variable and class namespcae
    def __init__(self):
        self.type = "TAF"           #instance variable and namespace
        self.maxspeed = 210
        self.func = "ESS"


c1 = car()
c2 = car()

print(c1.type, c1.maxspeed, c1.func, c1.company)
print(c2.type, c2.maxspeed, c2.func, c2.company)
