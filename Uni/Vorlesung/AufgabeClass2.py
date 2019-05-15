

class EineKlasse():

    def __init__(self, val):

        self.__eineVariable = val

if __name__ == "__main__":

    einObjekt = EineKlasse(123)
    print(einObjekt.eineVariable)

    einObjekt.eineVariable = 45

    print(einObjekt.eineVariable)

    einObjekt.eineNeuVariable = 666

    print( dir(einObjekt))