#You can inherit multiple times from a class, for example:

class MusicalInstruments:
    major_keys = 12

class StringInstruments(MusicalInstruments):
    type_of_wood = "Tonewood"
class Guitar(StringInstruments):
    def __init__(self):
        self.number_of_strings = 6
        print("The guitar is a musical instrument that consist of {} strings. It has {} major keys and it is made of {}.".format(self.number_of_strings, self.major_keys, self.type_of_wood))
guitar = Guitar()
