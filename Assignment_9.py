def main():

	i=0;
	count=0;
	while 1:
		if count>10:
			break;
		elif i%2==0:
			print(i,end="\t");
			count=count+1;
		i=i+1;

if __name__=="__main__":
	main();