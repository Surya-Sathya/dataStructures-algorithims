from abc import ABC

#Four Horseman of Classes -- 1) Abstraction
class Religions(ABC):
    pass
    def num_of_followers(self):
        pass

class Hinduism(Religions):
    def num_deities(self):
        print("There are a large number of deities in Hinduism in every period")
    def num_of_followers(self):
        print("3rd Largest")

class Islam(Religions):
    def idol_presence(self):
        print("False")
    def num_of_followers(self):
        print("Largest")

mughal_period_hinduism = Hinduism()
mughal_period_hinduism.num_of_followers()

mughal_period_Islam = Islam()
mughal_period_Islam.num_of_followers()
    