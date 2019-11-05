from MarvellousNum import *;
import functools as mod;

def AcceptList(arr,n):
	for i in range(n):
		print("Enter element {}: ".format(i+1),end=" ");
		arr.append(int(input()));

	return arr;


def ListPrime():

	print("Enter number of elements in list:");
	n=int(input());

	arr=list();

	arr=AcceptList(arr,n);

	print(arr);

	arr=list(filter(Prime,arr));

	print(arr);

	if(len(arr)!=0):
		ans=mod.reduce(Add,arr);
		print("Addition of prime numbers is ",ans);
	else:
		print("No prime elements");

if __name__=="__main__":
	ListPrime();
