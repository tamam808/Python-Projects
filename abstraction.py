from abc import ABC, abstractmethod 

class computer(ABC):
    def comp_type(self, os):
        print("My computer runs off of",os)
    @abstractmethod
    def comp_cost(self, cost):
        pass

class pc(computer):
    def comp_cost(self, cost):
        print("The cost of my computer was: ${}.00.".format(cost))

x = pc()

x.comp_type("Windows")

x.comp_cost("800")
