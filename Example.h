#ifndef EXAMPLE_H
#define EXAMPLE_H

namespace example {

    class Rectangle {
    private:
        int x0, y0, x1, y1;
    public:
        Rectangle();
        Rectangle(int x0, int y0, int x1, int y1);
        ~Rectangle();
        int getLength() const;
        int getHeight() const;
        int getArea() const;
        int getXPos() const;
        int getYPos() const;
        void move(int dx, int dy);
    };

    int getRectangleXPos(const Rectangle *rect);

    class Test {
    private:
        int id;
    public:
        Test();
        Test(int num);
        ~Test();
        Test& operator=(const Test& src);
        void printTest();
        void setID(int num);
    };

}

#endif

