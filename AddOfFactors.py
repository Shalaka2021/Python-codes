def AddFact(no):
	ans=0;
	for i in range(no//2,0,-1):
		if no%i==0:
			ans=ans+i;

	return ans;



def main():

	print("Enter a number:");
	no=int(input());

	ans=AddFact(no);

	print("Addition of factorial is ",ans);

if __name__=="__main__":
	main();