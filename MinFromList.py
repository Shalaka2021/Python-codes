def MkList(arr,n):
	for i in range(n):
		print("Enter element {}: ".format(i+1),end=" ");
		arr.append(int(input()));

	return arr;

def FndMin(arr):
	minm=arr[0];
	"""for i in range(len(arr)):
		if arr[i]<minm:
			minm=arr[i];"""

	minm=min(arr);

	return minm;

def main():

	print("Enter number of elements in list: ",end=" ");
	n=int(input());

	arr=list();

	arr=MkList(arr,n);

	minm=FndMin(arr);

	print("Minimum from list is ",minm);

if(__name__=="__main__"):
	main();