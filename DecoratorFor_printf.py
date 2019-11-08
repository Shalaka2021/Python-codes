def printf(str):		
	print(str);

def Decorator(oprintf):		
	def updateprint(str):		
		oprintf(str);
	return updateprint;


printf=Decorator(printf);


def main():

	print("In main");

	printf("I have been called through printf");


if __name__=="__main__":
	main();

