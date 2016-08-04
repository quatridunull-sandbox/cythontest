#include "Example.h"

#include <cstdio>

namespace example
{

Rectangle::Rectangle()
{
    x0 = y0 = x1 = y1 = 0;
    printf("----c++ default constructor was called\n");
}

Rectangle::Rectangle(int X0, int Y0, int X1, int Y1)
{
    x0 = X0;
    y0 = Y0;
    x1 = X1;
    y1 = Y1;
    printf("----c++ constructor was called\n");
}

Rectangle::~Rectangle()
{
    printf("----c++ destructor was called\n");
}

int
Rectangle::getLength() const
{
    return (x1 - x0);
}

int
Rectangle::getHeight() const
{
    return (y1 - y0);
}

int
Rectangle::getArea() const
{
    return (x1 - x0) * (y1 - y0);
}

int
Rectangle::getXPos() const
{
    return x0;
}

int
Rectangle::getYPos() const
{
    return y0;
}

void
Rectangle::move(int dx, int dy)
{
    x0 += dx;
    y0 += dy;
    x1 += dx;
    y1 += dy;
}

int
getRectangleXPos(const Rectangle *rect)
{
    /* printf("Using getRectangleXPos. Pointer value:%i\n", rect); */
    int xPos = rect->getXPos();
    /* printf("Position: %i\n", xPos); */
    return xPos;
}

Test::Test()
{
    id = -1;
    printf("----Test default constructor\n");
    return;
}

Test::Test(int num)
{
    id = num;
    printf("----Test Constructor: %i\n", id);
    return;
}

Test::Test(const Test& src)
{
    printf("----Test Copy Constructor: %i\n", id);
    id = src.id;
    return;
}

Test::~Test()
{
    printf("----Test Destructor: %i\n", id);
    return;
}

Test& Test::operator=(const Test& src)
{
    printf("----Test assignment operator: source: %i, destination: %i\n", src.id, id);
    id = src.id;
    return *this;
}

void Test::printTest() const
{
    printf("----Test ID: %i\n", id);
    return;
}

void Test::setID(int num)
{
    printf("----Change ID from %i to %i\n", id, num);
    id = num;
    return;
}

int Test::getID() const
{
    printf("----Get ID: %i\n", id);
    return id;
}

}

