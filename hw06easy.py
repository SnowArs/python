# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
	def __init__(self, coords_a, coords_b, coords_c):
		self.coords_a = coords_a
		self.coords_b = coords_b
		self.coords_c = coords_c
		
		def side(point1, point2):
			return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
			
		self.len_side_ab = side(self.coords_a, self.coords_b)
		self.len_side_bc = side(self.coords_b, self.coords_c)
		self.len_side_ca = side(self.coords_c, self.coords_a)

	def square(self):
		return 0.5 * abs((self.coords_b[0] - self.coords_a[0])
                                * (self.coords_c[1]- self.coords_a[1]) - (self.coords_c[0] - self.coords_a[0])
                                * (self.coords_b[1] - self.coords_a[1]))
	
			
	def perimetr(self):
		return self.len_side_ab + self.len_side_bc + self.len_side_ca
		
	def height(self):
		return self.square() / (self.len_side_ab / 2)
 
trian = Triangle( [1, 4], [5, 8], [4, 10])	

print(trian.square())
print(trian.perimetr())
print(trian.height())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trap():
	def __init__(self, coords_a, coords_b, coords_c, coords_d):
		self.coords_a = coords_a
		self.coords_b = coords_b
		self.coords_c = coords_c
		self.coords_d = coords_d
		
		def side(point1, point2):
			return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
			
		def square(len1, len2, len3):
			half_perim = (len1 + len2 + len3) / 2
			return math.sqrt(half_perim * (half_perim - len1)	* (half_perim - len2)	* (half_perim - len3))
			
		self.len_side_ab = side(self.coords_a, self.coords_b)
		self.len_side_bc = side(self.coords_b, self.coords_c)
		self.len_side_cd = side(self.coords_c, self.coords_d)
		self.len_side_da = side(self.coords_d, self.coords_a)
		self.diag_ac = side(self.coords_c, self.coords_a)
		self.diag_bd = side(self.coords_b, self.coords_d)
		self.perim = self.len_side_ab + self.len_side_bc + 															 	self.len_side_cd + self.len_side_da

# представим трапецию как 2 треугольника и сложим 2 площади этих треугольников

		self.area = square(self.len_side_ab, self.diag_bd, self.len_side_da) + square(self.diag_bd, self.len_side_bc, self.len_side_cd)
 
	def equal_or_not(self):
		if self.diag_ac == self.diag_bd:
			print('трапеция равнобедренная')
		else:
			print('трапеция не равнобедренная')

trap = Trap( [1, 1], [5, 5], [6, 5], [10, 1])	

print(trap.area)
print(trap.perim)
print(trap.equal_or_not())
