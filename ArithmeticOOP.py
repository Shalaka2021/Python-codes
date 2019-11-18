class Arithmetic:
	def __init__(self):
		self.val1=0;
		self.val2=0;

	def Accept(self,no1,no2):
		self.val1=no1;
		self.val2=no2;

	def Addition(self):
		return self.val1+self.val2;

	def Subtraction(self):
		return self.val1-self.val2;

	def Multiplication(self):
		return self.val1*self.val2;

	def Division(self):
		return self.val1/self.val2;

def main():

	obj1=Arithmetic();
	obj2=Arithmetic();
	obj3=Arithmetic();

	obj1.Accept(20,10);
	obj2.Accept(33,25);
	obj3.Accept(78,34);

	print(obj1.Addition());
	print(obj1.Subtraction());
	print(obj1.Multiplication());
	print(obj1.Division());


	print(obj2.Addition());
	print(obj2.Subtraction());
	print(obj2.Multiplication());
	print(obj2.Division());


	print(obj3.Addition());
	print(obj3.Subtraction());
	print(obj3.Multiplication());
	print(obj3.Division());

if __name__=="__main__":
	main();