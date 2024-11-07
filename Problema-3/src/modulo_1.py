#Modulo 1

def mcd_euclides(a, b):

    while b != 0:
        a, b = b, a % b
    return a
