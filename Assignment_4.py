ans=0;
def Sum(no):
	if(no!=0):
		global ans;
		ans=ans+no%10;
		Sum(no//10);
	return ans;

def main():
	no=int(input("Enter a no: "));

	ans=Sum(no);
	print("Answer is ",ans);

if __name__=="__main__":
	main();