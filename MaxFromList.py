def MkList(arr,n):
	for i in range(n):
		print("Enter elemet {}: ".format(i+1),end=" ");
		arr.append(int(input()));

	return arr;

def FndMax(arr):
	maxm=arr[0];
	for i in range(len(arr)):
		if(maxm<arr[i]):
			maxm=arr[i];

	#maxm=max(arr);

	return maxm;


def main():
	print("Enter number of elemets in list: ",end=" ");
	n=int(input());

	arr=list();

	arr=MkList(arr,n);

	maxm=FndMax(arr);

	print("Maximum element is: ",maxm);

if __name__=="__main__":
	main();
