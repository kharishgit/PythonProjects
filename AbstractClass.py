from abc import ABC , abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("Running")

class Programmer():
    def work(self,com):
        print("Fix bug")
        com.process()


class WhiteBoard(Computer):
    def write(self):
        print("Writing")

# com=Computer()
# com.process()
lap=Laptop()
lap.process()
prg=Programmer()
prg.work(lap)


