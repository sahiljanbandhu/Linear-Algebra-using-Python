"""       
import math
class complexcompute(object):
    def __init__(self,realPart,imgPart):
        self.realPart = realPart
        self.imgPart = imgPart
    def __add__(self,other):
        r1 = self.realPart
        i1 = self.imgPart
        r2 = other.realPart
        i2 = other.imgPart
        resultR = r1+r2
        resultI = i1+i2
        result = complex(result,resultI)
        return result
c1=complex(2,3)
c2=complex(5,4)
print(c1+c2)
c1=1+3j
c1.conjugate()
print(c1.conjugate())

"""

"""
import matplotlib .pyplot as plt
L=[-2+2j,-1+2j,0+2j,1+2j,2+2j,-1+4j,0+4j,1+4j]
X=[X.real for X in L]
Y=[X.imag for X in L]
plt.scatter(X,Y,color='red')
plt.show()
"""



"""
import matplotlib.pyplot as plt
triangle=[[3,5],[6,4],[1,2]]
coordinates_a = triangle[0]
coordinates_b = triangle[1]
coordinates_c = triangle[2]
def rotate90ccw(coordinates):
    print(coordinates)
    print("star coordinates:")
    old_x = coordinates[0]
    old_y = coordinates[1]
    new_x = old_y
    new_y = old_x
    print("End coordinates:")
    print([new_x,new_y])
    plt.scatter(old_x,old_y,color='red')
    plt.show()
    plt.scatter(new_x,new_y,color='blue')
    plt.show()
print("Let's rotate point A 90 degrees:")
rotate90ccw(coordinates_a)
print("Let's rotate point B 90 degrees:")
rotate90ccw(coordinates_b)
print("Let's rotate point C 90 degrees:")
rotate90ccw(coordinates_c)
print("==========")
"""


"""
import matplotlib.pyplot as plt
triangle=[[3,5],[6,4],[1,2]]
coordinates_a = triangle[0]
coordinates_b = triangle[1]
coordinates_c = triangle[2]
def rotate180ccw(coordinates):
    print(coordinates)
    print("star coordinates:")
    old_x = coordinates[0]
    old_y = coordinates[1]
    new_x = old_y
    new_y = old_x
    print("End coordinates:")
    print([new_x,new_y])
    plt.scatter(old_x,old_y,color='red')
    plt.show()
    plt.scatter(new_x,new_y,color='blue')
    plt.show()
print("Let's rotate point A 180 degrees:")
rotate180ccw(coordinates_a)
print("Let's rotate point B 180 degrees:")
rotate180ccw(coordinates_b)
print("Let's rotate point C 180 degrees:")
rotate180ccw(coordinates_c)
print("==========")
"""



"""
import matplotlib.pyplot as plt
triangle=[[3,5],[6,4],[1,2]]
coordinates_a = triangle[0]
coordinates_b = triangle[1]
coordinates_c = triangle[2]
def rotate270ccw(coordinates):
    print(coordinates)
    print("star coordinates:")
    old_x = coordinates[0]
    old_y = coordinates[1]
    new_x = old_y
    new_y = old_x
    print("End coordinates:")
    print([new_x,new_y])
    plt.scatter(old_x,old_y,color='red')
    plt.show()
    plt.scatter(new_x,new_y,color='blue')
    plt.show()
print("Let's rotate point A 270 degrees:")
rotate270ccw(coordinates_a)
print("Let's rotate point B 270 degrees:")
rotate270ccw(coordinates_b)
print("Let's rotate point C 270 degrees:")
rotate270ccw(coordinates_c)
print("==========")
"""

    























    
