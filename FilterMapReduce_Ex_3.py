import functools;

def AcceptList(arr,n):
	for i in range(n):
		print("Enter element {}: ".format(i+1),end=" ");
		arr.append(int(input()));

	return arr;

def Filterfunct(no):
	if no==1:
		return True;
	for i in range(no//2,0,-1):
		if(no%i==0):
			break;

	if i==1:
		return True;
	else:
		return False;

def Reducefunct(no1,no2):
	if no1>no2:
		return no1;
	else:
		return no2


def main():
	n=int(input("Enter number of elements: "));

	arr=list();

	arr=AcceptList(arr,n);

	arr=list(filter(Filterfunct,arr));

	print("List after filter=",arr);

	if len(arr)==0:
		return ;

	arr=list(map(lambda no:no*2,arr));

	print("List after map=",arr);

	ans=functools.reduce(Reducefunct,arr);

	print("Output after reduce=",ans);

if __name__=="__main__":
	main();
