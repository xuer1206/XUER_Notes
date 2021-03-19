class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print("The restaurant name is " + self.restaurant_name.title() +".")
		print("The cuisine type is " + self.cuisine_type.title() + ".")
		
	def open_restaurant(self):
		print("The restaurant is opening.")
		
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
	#初始化父类属性
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['caomei','chocklate','sweet']
	
	def read_flavors(self):
		print(self.flavors)
	
		
my_restaurant = IceCreamStand('drink','sweet food')
print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.read_flavors()


