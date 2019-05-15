import math



def UmfangInput():

    r = float(input("Radius?"))
    pi = float(math.pi)

    U = 2 * pi * r

    A = pi * r**2

    print('Umfang: %f \nFläche: %f'%(U,A))

if __name__ == "__main__":
    UmfangInput()