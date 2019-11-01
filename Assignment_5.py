def main():

	print("Enter a number:");
	no=int(input());

	for i in range(no//2,0,-1):
		if no%i==0:
			break;

	if i==1:
		print("It is Prime number");
	else:
		print("It is Not Prime number");

if __name__=="__main__":
	main();