def main():

	print("Enter a number:");
	no=int(input());

	for i in range(no):
		for j in range(0,no-i):
			print("*",end="\t");
		print("\n");

if __name__=="__main__":
	main();