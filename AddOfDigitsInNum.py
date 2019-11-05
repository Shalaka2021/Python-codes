def AddOfDigit(no):
	rem=0;
	while no>0:
		rem=rem+no%10;
		no=no//10;

	return rem;

def main():
	print("Enter a number:");
	no=int(input());

	ans=AddOfDigit(no);

	print(ans);

if __name__=="__main__":
	main();
