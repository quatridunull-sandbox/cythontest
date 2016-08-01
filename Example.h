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
        int getLength();
        int getHeight();
        int getArea();
        int getXPos();
        int getYPos();
        void move(int dx, int dy);
    };

}

#endif

