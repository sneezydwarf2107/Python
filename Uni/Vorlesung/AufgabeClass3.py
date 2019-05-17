class P():
    def __init__(self, x):
        self.__x = x
        print(x)

    def __getx(self):
        return self.__x

    def __setx(self, x):
        self.__x = x

    def __delx(self):
        del self.__x

    doc = "Beschreibung der Klasse"

    x = property(__getx, __setx, __delx, doc)


if __name__ == "__main__":
    o = P("Bogi ist eine dumme Sau")
    o.x