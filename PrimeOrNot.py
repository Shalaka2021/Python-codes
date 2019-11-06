def main():

	print("Enter a number:");
	no=int(input());
	i=0;
	if no!=1:
		for i in range(no//2,0,-1):
			if no%i==0:
				break;

	if i==1:
		print("It is Prime number");
	else:
		print("It is Not Prime number");

if __name__=="__main__":
	main();
