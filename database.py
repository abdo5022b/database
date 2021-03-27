import time , os , sys , getpass
#set a password to get access
while getpass.getpass("\033[1;32;40mPassword >> \033[0;37;40m >>") != "1bd0":
	print("\033[1;31;40m =====PASSWORD WRONG===== \033[0;37;40m".center(75))
	time.sleep(0.3)
	os.system("clear")
	
	
else:
	print("\033[1;35;33m =====PASSWORD CORRECT===== \033[0;37;40m".center(75))
	time.sleep(0.5)
	os.system("clear")
print("welcome \033[1;35;40m")
#this is the data that you want to check
h = {
"abderrahman" : "Name : Abderrahman \nF.name : Sakit \nAge :?? \nBirthday :??/??/????  "
} 
f = str(input("print a name \033[1;32;40m  : "))
# a fonction to restart the program 
def restart_program():

   python = sys.executable

   os.execl(python, python, * sys.argv)

   curdir = os.getcwd()
try:
	print(  "\033[0;37;40m" +h[f] )
except:
	print("Not Found")
	restart_program()
#now we are going to make file that contains the data you searched
try:
	def file():
		os.chdir("/sdcard")
		g = open(f+".txt","w")
		g.write(h[f]+ "\n" +"\nDESIGNED BY A.SAKIT")
		g.close()
	#if f != h:
#		print()
	file()
except:
	print("THIS NAME DOES'NT EXIST")
	restart_program()
#	restart_program()
	

	

	
