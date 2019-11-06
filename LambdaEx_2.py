def main():
	no1=int(input("Enter no1: "));
	no2=int(input("Enter no2: "));

	fptr=lambda no1,no2:no1*no2;

	print(fptr(no1,no2));


if __name__=="__main__":
	main();