import math

class Rectangle():
    def __init__(self, height, width):
        self._area = height * width
        self._diagonal = math.sqrt((height ** 2) + (width ** 2))

    def area(self):
        return f"面積:{self._area:.2f}（cm²）"
    
    def diagonal(self):
        return f"対角線の長さ:{self._diagonal:.2f}（cm）"
    
    def __str__(self):
        return f"面積: {self.area()}（cm²）, 対角線の長さ: {self.diagonal()}(cm）" 

rectangle1 = Rectangle(height=5, width=6)
print(rectangle1._area)  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
