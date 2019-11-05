from Arithmetic import *

def main():

	print("Enter no1:");
	no1=int(input());

	print("Enter no2:");
	no2=int(input());

	ans=Add(no1,no2);
	print("Addition is:",ans);

	ans=Sub(no1,no2);
	print("Subtraction is:",ans);

	ans=Mul(no1,no2);
	print("Multiplication is:",ans);

	ans=Div(no1,no2);
	print("Division is:",ans);

if __name__=="__main__":
	main();