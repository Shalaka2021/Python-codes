def MkList(arr,n):
	for i in range(n):
		print("Enter element {}: ".format(i+1),end=" ");
		arr.append(int(input()));

	return arr;

def FreqCount(arr,srchElmnt):
	frqcnt=0;
	for i in range(len(arr)):
		if(arr[i]==srchElmnt):
			frqcnt=frqcnt+1;

	return frqcnt;

def main():

	print("Enter number of elements in list: ",end=" ");
	n=int(input());

	arr=list();

	arr=MkList(arr,n);

	print("Enter element to find frequency:");
	search=int(input());

	ans=FreqCount(arr,search);

	print("Frequency count of element is ",ans);

if __name__=="__main__":
	main();
