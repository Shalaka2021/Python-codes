import functools;

def AcceptList(arr,n):
	for i in range(n):
		print("Enter element {}: ".format(i+1),end=" ");
		arr.append(int(input()));

	return arr;

def main():
	n=int(input("Enter number of elements in list: "));

	arr=list();

	arr=AcceptList(arr,n);

	arr=list(filter(lambda no:not(no%2),arr));

	print("List after filter=",arr);

	if(len(arr)==0):
		return;

	arr=list(map(lambda no:no**2,arr));

	print("List after map=",arr);

	ans=functools.reduce(lambda no1,no2:no1+no2,arr);

	print("Output after reduce=",ans);

if __name__=="__main__":
	main();

