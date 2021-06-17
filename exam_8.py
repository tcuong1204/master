from abc import ABC, abstractmethod

print("FIND THE ACREAGE")
print("You want to find acreage of? (Enter number)")


class geometry(ABC):  # abstrac: Khong the su dung truc tiep
    def __init__(self):
        pass

    def set(self, value):
        print("The acreage:")
        self.value = value

    @abstractmethod
    def area(self):
        pass


class Circle(geometry):
    print("0. Find acreage of the Circle")

    def __init__(self):
        self.__pi = 3.141519  # Dong goi ngan chan sua doi

    def area(self):  # ke thua lop cha geometry
        return self.value * self.value * self.__pi

    def call(self):
        c = Circle()
        c.set(float(input("Radius: ")))
        print(c.area())


class Square(geometry):
    print("1. Find acreage of the Square")

    def area(self):
        return self.value * self.value

    def call(self):
        s = Square()
        s.set(float(input("Edge: ")))
        print(s.area())


class Rectangle(geometry):
    print("2. Find acreage of the Rectangle")

    def set(self, value, value1):
        self.value = value
        self.value1 = value1

    def area(self):
        return self.value * self.value1

    def call(self):
        r = Rectangle()
        r.set(float(input("Length: ")), float(input("Width: ")))
        print(r.area())


class Triangle(Rectangle, geometry):  # Rectangle
    print("3. Find acreage of the Triangle")

    def area(self):
        return self.value * self.value1 / 2  # Tinh da hinh ve cong thuc tinh

    def call(self):
        t = Triangle()
        t.set(float(input("Edge: ")), float(input("Height: ")))
        print(t.area())


a = [Circle(), Square(), Rectangle(), Triangle()]
b = int(input())
a[b].call()

class Triangle2(Rectangle, geometry):  # Rectangle
    print("3. Find acreage of the Triangle")

    def area(self):
        return self.value * self.value1 / 2  # Tinh da hinh ve cong thuc tinh

    def call(self):
        t = Triangle()
        t.set(float(input("Edge: ")), float(input("Height: ")))
        print(t.area())


a = [Circle(), Square(), Rectangle(), Triangle()]
b = int(input())
a[b].call()
