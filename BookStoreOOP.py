class BookStore:
	NoOfBooks=0;
	def __init__(self,name,author):
		self.Name=name;
		self.Author=author;
		BookStore.NoOfBooks+=1;

	def Display(self):
		print("{} by {}.No of books: {}".format(self.Name,self.Author,BookStore.NoOfBooks));

def main():
	"""name=input("Enter name of book: ");
	author=input("Enter auhtor of book: ");"""

	obj1=BookStore("Linux System Programming","Robert Love");
	obj1.Display();

	"""name=input("Enter name of book: ");
	author=input("Enter author of book: ");"""
	
	obj2=BookStore("C Programming","Dennis Ritchie");
	obj2.Display();	

if __name__=="__main__":
	main();
