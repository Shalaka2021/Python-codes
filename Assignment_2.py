def main():

	print("Enter a number:");
	no=int(input());

	for i in range(no):
		for j in range(no):
			print("*",end="\t");
		print("\n");

if __name__=="__main__":
	main();