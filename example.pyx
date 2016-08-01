# Declare class and add public attributes
cdef extern from "Example.h" namespace "example":
    cdef cppclass Rectangle:
        Rectangle()
        Rectangle(int, int, int, int)
        int getLength()
        int getHeight()
        int getArea()
        int getXPos()
        int getYPos()
        void move(int, int)

# Heap-allocated rectangle

#cdef Rectangle *rec = new Rectangle(1, 2, 3, 4)
#cdef int recLength = rec.getLength()
#cdef int recHeight = rec.getHeight()
#cdef int getArea = rec.getArea()
#cdef int getXPos = rec.getXPos()
#cdef int getYpos = rec.getYPos()

#del rec

# Stack-allocated rectangle
# cdef Rectangle rec

# create Cython wrapper class
cdef class PyRectangle:
    cdef Rectangle *thisptr      # hold a C++ instance which we're wrapping
    #def __cinit__(self):
        #self.thisptr = new Rectangle()    # cannot overload python constructors
    def __cinit__(self, int x0, int y0, int x1, int y1):
        self.thisptr = new Rectangle(x0, y0, x1, y1)
    def __dealloc__(self):
        del self.thisptr
    def getLength(self):
        return self.thisptr.getLength()
    def getHeight(self):
        return self.thisptr.getHeight()
    def getArea(self):
        return self.thisptr.getArea()
    def getXPos(self):
        return self.thisptr.getXPos()
    def getYPos(self):
        return self.thisptr.getYPos()
    def move(self, dx, dy):
        self.thisptr.move(dx, dy)
