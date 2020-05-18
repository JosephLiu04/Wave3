from math import sqrt
Side1 = float(input("Input the length of the shorter first side:"))
Side2 = float(input("Input the length of the shorter second side: "))

def Pythag_theorem():
    Side3 = sqrt((Side1 * Side1) + (Side2 * Side2)) 
    return Side3

print("The length of the hypotenuse is", str(Pythag_theorem()))