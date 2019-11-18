def Factorial(no):
	if(no==1):
		return 1;
	return no*Factorial(no-1);

def main():
	no=int(input("Enter a no: "));

	ans=Factorial(no);
	print("Factorial is ",ans);

if __name__=="__main__":
	main();