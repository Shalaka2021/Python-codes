def mybin(no):
	if(no==0):
		return ;
	mybin(no//2);
	print(no%2,end =" ");

def myoct(no):
	if(no==0):
		return ;
	myoct(no//8);
	print(no%8,end=" ");

def myhex(no):
	atof=['a','b','c','d','e','f'];
	if(no==0):
		return ;
	myhex(no//16);
	#print(no);
	x=no%16;
	if(x<10):
		print(x,end=" ");
	else:
		print(atof[x%10],end=" ");


def main():
	no=int(input("Enter decimal no: "));

	print("Decimal no: ",no);
	print("Binary no:");
	mybin(no);
	print("\nOctal no: ");
	myoct(no)
	print("\nHexadecimal no: ");
	myhex(no)

if __name__=="__main__":
	main();