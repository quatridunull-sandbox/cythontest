import example

class PyRect(example.PyRectangle):
    memberVariable = example.PyTest(0)

    def __init__(self, a, b, c, d):
        self.memberVariable = example.PyTest(1)
        return

    def getXPos(self):
        print("Using derived class method!")
        return super(PyRect, self).getXPos()

    def testDelete(self):
        #test = self.memberVariable
        #del test
        self.memberVariable = example.PyTest(2)

print("--------------------")

print("rect = example.PyRectangle(1, 2, 3, 4)")
rect = example.PyRectangle(1, 2, 3, 4)
print("")

print("rectDerived = PyRect(5, 6, 7, 8)")
rectDerived = PyRect(5, 6, 7, 8)
print("")

print("--------------------")

print("rect xPos:", rect.getXPos())
print("rectDerived xPos:", rectDerived.getXPos())
print("")

print("rect yPos:", rect.getYPos())
print("rectDerived yPos:", rectDerived.getYPos())
print("")

print("--------------------")

print("TEST POLYMORPHISM")
print("")

print("-----")
print("C++")
print("")
print("rect xPos using c++ getRectangleXPos():", example.getRectangleXPos_test_cpp(rect))
print("")
print("rectDerived yPos using c++ getRectangleXPos():", example.getRectangleXPos_test_cpp(rectDerived))
print("")

print("-----")
print("Cython")
print("")
print("rect xPos using cython getRectangleXPos():", example.getRectangleXPos_test_cython(rect))
print("")
print("rectDerived yPos using cython getRectangleXPos():", example.getRectangleXPos_test_cython(rectDerived))
print("")

print("--------------------")

print("TEST DELETE")
print("")

print("call rectDerived.testDelete()")
rectDerived.testDelete()
print("")

print("--------------------")

print("Move both by (5, 5)")
rect.move(5, 5)
rectDerived.move(5, 5)
print("")

print("--------------------")

print("rect xPos:", rect.getXPos())
print("rectDerived xPos:", rectDerived.getXPos())
print("")

print("--------------------")

print("rect yPos:", rect.getYPos())
print("rectDerived yPos:", rectDerived.getYPos())
print("")

print("--------------------")

del rect
print("")
del rectDerived
print("")
exit()

