def main():

	print("Enter a number:");
	no=int(input());

	for i in range(0,no):
		for j in range(0,i+1):
			print(j+1,end="\t");
		print("\n");

if __name__=="__main__":
	main();
