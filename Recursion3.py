def Pattern(no):
	if(no!=0):
		print(no,end=" ");
		Pattern(no-1);

def main():
	no=int(input("Enter a no: "));

	Pattern(no);

if __name__=="__main__":
	main();