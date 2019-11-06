import functools;

def AcceptList(arr,n):
	for i in range(0,n,1):
		print("Enter element {}: ".format(i+1),end=" ");
		arr.append(int(input()));

	return arr;

def FilterList(no):
	if no>=70 and no<=90:
		return True;
	else:
		return False;

def MapList(no):
	return no+10;

def ReduceList(no1,no2):
	return no1*no2;



def main():
	print("Enter number of elements in list:");
	n=int(input());

	arr=list();

	arr=AcceptList(arr,n);

	arr=list(filter(FilterList,arr));

	print("List after filter=",arr);

	if(len(arr)==0):
		return;

	arr=list(map(MapList,arr));

	print("List after map=",arr);

	ans=functools.reduce(ReduceList,arr);

	print("Output of reduce=",ans);

if __name__=="__main__":
	main();

