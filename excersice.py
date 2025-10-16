#Write an object oriented program to create a precious stone. Not more than 5 precious stones can be held in possession at a given point of time. If there are more than 5 precious stones, delete the first stone and store the new one.

class Traveler:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.gemes = []
    counter = 0
    def gemes_collection(self):
        counter = 0
        if len(self.gemes) != 0:
            for geme in self.gemes:
                print(geme.name, ", ", geme.weight, ", $ ", geme.value)
        else:
            print("Youre poor")
    def add_geme(self, geme):
        if len(self.gemes) >= 5:
            print("You can have any other geme. Bag is full of stones.")
        else:
            self.gemes.append(geme)

class Geme:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
    

geme1 = Geme("Emerald", "293gm", 12000)
geme2 = Geme("Emerald", "293gm", 12000)
geme3 = Geme("Emerald", "293gm", 12000)
geme4 = Geme("Emerald", "293gm", 12000)
geme5 = Geme("Emerald", "293gm", 12000)
geme6 = Geme("Emerald", "293gm", 12000)
maximo = Traveler("Maximo", 24)
raul = Traveler("Raul", 24)
raul.gemes_collection()
maximo.add_geme(geme1)
maximo.add_geme(geme2)
maximo.add_geme(geme3)
maximo.add_geme(geme4)
maximo.add_geme(geme5)
maximo.add_geme(geme6)
maximo.gemes_collection()
