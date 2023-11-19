# import math

# class Square:
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         area =  self.side ** 2
#         return f"{area:.2f}" if area % 1 != 0 else f"{area:.0f}"
    
#     def diagonal(self):
#         diagonal =  self.side * math.sqrt(2)
#         return f"{diagonal:.2f}" if diagonal % 1 != 0 else f"{diagonal:.0f}"

# square1 = Square(side=1.5)
# print(square1.area())  # 2.25
# print(square1.diagonal())  # 2.12

# square2 = Square(side=15)
# print(square2.area())  # 225
# print(square2.diagonal())  # 21.21
import math


class Square:
    def __init__(self, side):
        self._side = side
        self._area = None  # 初期値を設定しておく
        self._diagonal = None 
        
    def area(self):
        self._area = self._side ** 2
        return self._area
    
    def diagonal(self):
        self._diagonal = self._side * math.sqrt(2)
        return self._diagonal
    
    def __str__(self):
        area_str = f"{self.area():.2f}" if self.area() % 1 != 0 else f"{self.area():.0f}"
        diagonal_str = f"{self.diagonal():.2f}" if self.diagonal() % 1 != 0 else f"{self.diagonal():.0f}"
        return f"正方形の面積: {area_str}（cm²）対角線の長さ: {diagonal_str}（cm）"

square1 = Square(side=1.5)
square1.area()
square1.diagonal()
print(square1)  # 正方形の面積: 2.25、対角線の長さ: 2.12

square2 = Square(side=15)
square2.area()
square2.diagonal()
print(square2)  # 正方形の面積: 225、対角線の長さ: 21.21

user_input = int(input("正方形の1辺の長さを入力してください > "))
user_square = Square(user_input)

print(user_square)
