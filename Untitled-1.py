import numpy as np

class Triangle:
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def sideA(self):
        return int(self.sideA)

    def sideB(self):
        return int(self.sideB)

    def sideC(self):
        return int(self.sideC)

    def perimeter(self):
        return self.sideA + self.sideB + self.sideC

    def area(self):
        return np.sqrt(self.perimeter() * (self.perimeter()-self.sideA) * (self.perimeter()-self.sideB) * (self.perimeter()-self.sideC))
    
    def input(self):
        self.sideA = int(input("Enter sideA: "))
        self.sideB = int(input("Enter sideB: "))
        self.sideC = int(input("Enter sideC: "))
		
    def output(self):
        print("sideA = " + str(self.sideA))
        print("sideB = " + str(self.sideB))
        print("sideC = " + str(self.sideC))
        print("perimeter = " + str(self.perimeter()))
        print("area = " + str(self.area()))

class Quadrangle(Triangle):
    def __init__(self, sideA, sideB, sideC, sideD, diagonalE, diagonalF):
        super().__init__(sideA, sideB, sideC)
        self.sideD = sideD
        self.diagonalE = diagonalE
        self.diagonalF = diagonalF

    def sideD(self):
        return int(self.sideD)

    def diagonalE(self):
        return int(self.diagonalE)

    def diagonalF(self):
        return int(self.diagonalF)
        
    def perimeter(self):
        return int(self.sideA + self.sideB + self.sideC + self.sideD)

    def area(self):
        return int(np.sqrt((4*(self.diagonalE*self.diagonalE)*(self.diagonalF*self.diagonalF) - (self.sideB**2 + self.sideD**2 - self.sideA**2 - self.sideC**2))/16))

    def input(self):
        super().input()
        self.sideD = int(input("Enter sideD: "))
        self.diagonalE = int(input("Enter diagonalE: "))
        self.diagonalF = int(input("Enter diagonalF: "))


    def output(self):
        super().output()
        print("SideD: " + str(self.sideD))
        print("diagonalE: " + str(self.diagonalE))
        print("diagonalF: " + str(self.diagonalF))




pc1 = Triangle(1, 1200, 12)
pc2 = Triangle(2, 3200, 8)

lt1 = Quadrangle( 4000, 10, 3072, 345, 234, 234)
lt2 = Quadrangle( 2500, 6, 3072, 24, 234, 234)

pc1.output()
print()
pc2.output()
print()
lt1.output()
print()
lt2.output()
print()
pc1.input()
print()
pc1.output()
print()
lt1.input()
print()
lt1.output()

