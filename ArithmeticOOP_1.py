class Arithmetic:
	def __init__(self,val):
		self.Value=val;

	def ChkPrime(self):
		if(self.Value==1):
			return False;
		for i in range(self.Value//2,1,-1):
			if(self.Value%i==0):
				return False;
		return True;

	def Factors(self):
		arr=[1];
		for i in range(2,(self.Value//2)+1,1):
			if(self.Value%i==0):
				arr.append(i);
		arr.append(self.Value);
		return arr;

	def ChkPerfect(self):
		if((self.SumFactors()-self.Value)==self.Value):
			return True;
		return False;

	def SumFactors(self):
		arr=list();
		arr=self.Factors();
		sum=0;
		for i in range(len(arr)):
			sum=sum+arr[i];
		return sum


def main():
	no=int(input("Enter a no: "));

	obj1=Arithmetic(no);
	flag=obj1.ChkPrime();
	print("No is prime: ",flag);

	arr=obj1.Factors();
	print(arr);

	flag=obj1.ChkPerfect();
	print("No is perfect: ",flag);

	ans=obj1.SumFactors();
	print("Sum of factors is ",ans);

if __name__=="__main__":
	main();

