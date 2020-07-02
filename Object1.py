# Define class
class computer:

    def __init__(self,cpu ,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        # self.cpu = cpu
        # self.ram = ram
        print("config is", self.cpu, self.ram)


com1 = computer("i7",8)
com2 = computer("i9",16)

com1.config()
com2.config()