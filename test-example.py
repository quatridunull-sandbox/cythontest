import example
from copy import deepcopy

print("\n")

class PyRect(example.PyRectangle):
    memberVariable = example.PyTest(0)

    def __init__(self, a, b, c, d):
        self.memberVariable = example.PyTest(1)
        return

    def getXPos(self):
        print("Using derived class method!")
        return super(PyRect, self).getXPos()

    def testDelete(self):
        print("--1--")
        print("test = example.PyTest(100)")
        test = example.PyTest(100)
        test.printTest()
        print("")
        print("--2--")
        print("test2 = test")
        test2 = test
        test2.printTest()
        print("")
        print("--3--")
        print("test3 = deepCopy(test)")
        test3 = deepcopy(test)
        #test3 = test
        test3.printTest()
        print("")
        print("--4--")
        print("Set ID of test2 to 99999")
        test2.setID(99999)
        print("Set ID of test3 to 33333")
        test2.setID(33333)
        print("")
        print("--5--")
        print("test")
        test.printTest()
        print("")
        print("--6--")
        print("test2")
        test2.printTest()
        print("")
        print("--7--")
        print("test3")
        test3.printTest()
        print("")
        print("--8--")
        print("delete test3")
        del test3
        print("")
        print("--9--")
        print("delete test2")
        del test2
        print("")
        print("--10--")
        print("delete test")
        del test
        print("")
        print("--11--")
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

print("TEST DELETION AND COPYING")
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

