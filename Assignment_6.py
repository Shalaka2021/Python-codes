def ChkTyp(no):
	if no<0:
		print("Negative number");
	elif no==0:
		print("Zero");
	else:
		print("Positive number");

def main():
	print("Enter a number:");
	no=int(input());

	ChkTyp(no);

if __name__=="__main__":
	main();