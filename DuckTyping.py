

class pycharm:

    def execute(self):
        print("date")
        print("time")


class myeditor:       # it gives more feature

    def execute(self):
        print("date")
        print("time")
        print("Compile")
        print("run")

class laptop:

    def code(self,ide):
        ide.execute()


#ide = pycharm()
ide = myeditor()

lap = laptop()
lap.code(ide)