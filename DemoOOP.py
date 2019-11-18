class Demo:
	Value=0;

	def __init__(self,val1,val2):
		self.no1=val1;
		self.no2=val2;

	def Fun(self):
		print(self.no1,self.no2);
	def Gun(self):
		print(self.no1,self.no2);

def main():
	no1=int(input("Enter no1: "));
	no2=int(input("Enter no2: "));

	obj1=Demo(no1,no2);
	obj2=Demo(no1,no2);

	obj1.Fun();
	obj2.Fun();
	obj1.Gun();
	obj2.Gun();

	obj3=Demo(11,21);
	obj4=Demo(51,101);

	obj3.Fun();
	obj4.Fun();
	obj3.Gun();
	obj4.Gun();


if __name__=="__main__":
	main();