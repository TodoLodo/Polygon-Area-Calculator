class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        self.__width: int | float = width
        self.__height: int | float = height

    @property
    def width(self) -> int | float:
        return self.__width

    @property
    def height(self) -> int | float:
        return self.__height

    def set_width(self, _width: int | float) -> None:
        self.__width = _width

    def set_height(self, _height: int | float) -> None:
        self.__height = _height

    def get_area(self) -> int | float:
        return self.width * self.height

    def get_perimeter(self) -> int | float:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> int | float:
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self) -> str:
        return f"{'*'*self.width}\n"*self.height if self.height <= 50 and self.width <= 50 else "Too big for picture."

    def get_amount_inside(self, _rect) -> int:
        re = 0
        if self.width >= _rect.width and self.height >= _rect.height:
            re += (self.width // _rect.width) * (self.height // _rect.height)
        return re

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length: int | float):
        super().__init__(length, length)

    def set_side(self, length: int | float) -> None:
        self._Rectangle__height = length
        self._Rectangle__width = length

    def set_width(self, _width: int | float) -> None:
        self.set_side(_width)

    def set_height(self, _height: int | float) -> None:
        self.set_side(_height)

    def __str__(self) -> str:
        return f"Square(side={self.width})"
