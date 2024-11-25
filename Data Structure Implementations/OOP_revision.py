from abc import ABC, abstractmethod

#Four Horseman of Classes -- 1) Abstraction
class Religions(ABC):
    #If you want to add attributes every subclass must have, then 1) Create an init in the abstract class
    def __init__(self, origin, founder):
        self.country_origin = origin
        self.founder = founder

    @abstractmethod
    def num_of_followers(self):
        pass

    #As seen from below, the point of an abstract class is to define exactly what each subclass must contain (attributes, methods)
    #For religiions there has to be num_of_followers function
    #Can't instantiate abstract class Islam without an implementation for abstract method 'num_of_followers'

class Hinduism(Religions):
    def __init__(self, origin, founder, num_deities):
        super().__init__(origin, founder) 
        self.num_deities = num_deities
    #Python actually automatically calls the parent constructor, unless you override it with additional logic here
    #The additional attribute added in this case is num_deities actually

    def num_deities(self):
        print("There are a large number of deities in Hinduism in every period")
    def num_of_followers(self):
        print("3rd Largest")

class Islam(Religions):
    #We don't need to call super here
    def idol_presence(self):
        print("False")
    def num_of_followers(self):
        print("Largest")

mughal_period_hinduism = Hinduism()
mughal_period_hinduism.num_of_followers()

mughal_period_Islam = Islam(origin = "Mecca, Saudi Arabia", founder = "Unknown")
mughal_period_Islam.num_of_followers()

#TODO: Hidden Unit
#2 -- Encapsulation
#3 -- Inheritence
#4 -- Mutability