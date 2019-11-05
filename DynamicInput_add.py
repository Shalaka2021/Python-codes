def MkList(arr,n):
	for i in range(n):
		print("Enter no {}: ".format(i+1),end=" ");
		no=int(input());
		arr.append(no);

	return arr;

def Add(arr):
	ans=0;
	for i in range(0,len(arr),1):
		ans=ans+arr[i];

	#ans=sum(arr);

	return ans;

def main():
	print("Enter number of elements in list:");
	n=int(input());

	arr=list();

	arr=MkList(arr,n);

	ans=Add(arr);
	print("Addition of list elements is: ",ans);

if(__name__=="__main__"):
	main();