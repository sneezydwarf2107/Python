
class Begruessung():

    def __init__(self, Name):
        self.Name = Name

    def sagHallo(self):
        print("Hallo ", self.Name, "!", sep='', end='')
        print("Test")



if __name__ == "__main__":

    MeinObjekt = Begruessung("Welt")
    #MeinObjekt.sagHallo()