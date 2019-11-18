class Circle:
	PI=3.14;
	def __init__(self):
		self.Radius=0.0;
		self.Area=0.0;
		self.Circumference=0.0;

	def Accept(self,radius):
		self.Radius=radius;

	def CalculateArea(self):
		self.Area=Circle.PI*self.Radius**2;

	def CalculateCircumference(self):
		self.Circumference=2*Circle.PI*self.Radius;

	def Display(self):
		print("Radius is ",self.Radius);
		print("Area is ",self.Area);
		print("Circumference is ",self.Circumference);


def main():
	r=int(input("Enter radius: "));

	obj1=Circle();
	obj1.Accept(r);
	obj1.CalculateArea();
	obj1.CalculateCircumference();
	obj1.Display();

	obj2=Circle();
	obj2.Accept(9);
	obj2.CalculateArea();
	obj2.CalculateCircumference();
	obj2.Display();

if __name__=="__main__":
	main();

