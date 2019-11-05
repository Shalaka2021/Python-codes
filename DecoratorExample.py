def sub(no1,no2):	
	return no1-no2;

def Decoratorfunct(sub):		
	def updatorfunct(no1,no2):	
		if no1<no2:
			no1,no2=no2,no1;
		return sub(no1,no2);

	return updatorfunct;

sub=Decoratorfunct(sub);	

def main():

	print("Enter no1:");
	no1=int(input());
	print("Enter no2:");
	no2=int(input());
	
	ans=sub(no1,no2);
	print("Result is ",ans);

if __name__=="__main__":
	main();