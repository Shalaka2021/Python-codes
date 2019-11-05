def Add(no1,no2):
	return no1+no2;

def main():
	print("Enter 1st number:");
	no1=int(input());
	print("Enter 2nd number:");
	no2=int(input());
	
	ans=Add(no1,no2);

	print("Result is:",ans);

if __name__=="__main__":
	main();