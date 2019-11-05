def main():

	print("Enter a number:");
	no=int(input());

	for i in range(0,no):
		for j in range(0,no):
			print(j+1,end="\t");
		print("\t");

if __name__=="__main__":
	main();