class BankAccount:
	ROI=10.5;
	def __init__(self,name,amount):
		self.Name=name;
		self.Amount=amount;

	def Deposit(self,amount):
		self.Amount=self.Amount+amount;

	def Withdraw(self,amount):
		self.Amount=self.Amount-amount;

	def Display(self):
		print("Name: ",self.Name);
		print("Amount: ",self.Amount);

	def CalculateInterest(self):
		print("Rate of Interest is ",self.ROI);

def main():

	obj1=BankAccount("Jay",5000);
	print("Account created:- ");
	obj1.Display();
	obj1.Withdraw(800);
	print("After withdrawal:- ");
	obj1.Display();
	obj1.Deposit(500);
	print("After deposit:- ");
	obj1.Display();

	obj2=BankAccount("Ketan",3000);
	print("Account created:- ");
	obj2.Display();
	obj2.Withdraw(800);
	print("After withdrawal:- ");
	obj2.Display();
	obj2.Deposit(500);
	print("After deposit:- ");
	obj2.Display();

if __name__=="__main__":
	main();