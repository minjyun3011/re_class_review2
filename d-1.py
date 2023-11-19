class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14 * (self.radius ** 2)
        self.perimeter = 3.14 * (self.radius) * 2

    # def area(self):
    #     return 3.14 * (self.radius ** 2)
    
    # def perimeter(self):
    #     return 3.14 * (self.radius) * 2

    def __str__(self) -> str:
        return f"{self.area}" f"{self.perimeter}"


# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area)  # 3.14
print(circle1.perimeter)  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area)  # 28.27
print(circle3.perimeter)  # 18.85
