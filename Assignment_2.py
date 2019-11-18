i=1;
def Pattern(no):
	global i;
	if(no!=0):
		print(i,end=" ");
		i+=1;
		Pattern(no-1);

def main():
	no=int(input("Enter a no: "));

	Pattern(no);

if __name__=="__main__":
	main();