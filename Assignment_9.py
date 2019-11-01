def TotCount(no):
	count=0;
	while no>0:
		count=count+1;
		no=no//10;

	return count;

def main():
	print("Enter a  number:");
	no=int(input());

	ans=TotCount(no);

	print(ans);

if __name__=="__main__":
	main();