def DivBy5(no):
	if no%5==0:
		return True;
	else:
		return False;

def main():
	print("Enter a number:");
	no=int(input());

	boolval=DivBy5(no);

	print(boolval);

if __name__=="__main__":
	main();