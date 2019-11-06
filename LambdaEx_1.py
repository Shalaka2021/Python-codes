def main():
	no=int(input("Enter a number: "));

	fptr=lambda no:2**no;

	print(fptr(no));

if(__name__=="__main__"):
	main();