def facto(no):
	if no==1:
		return 1;
	return no*facto(no-1);



def main():

	print("Enter number to find factorial");
	no=int(input());

	ans=facto(no);

	print("Factorial is ",ans);

if __name__=="__main__":
	main();