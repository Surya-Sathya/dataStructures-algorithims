from abc import ABC

class Religions(ABC):
    pass

class Hinduism(Religions):
    def num_deities(self):
        print("There are a large number of deities in Hinduism in every period")


class Islam(Religions):
    def idol_presence():
        print("False")

mughal_period_hinduism = Hinduism()
mughal_period_hinduism.num_deities()
    