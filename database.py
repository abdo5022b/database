import time , os , sys , getpass
while getpass.getpass("\033[1;32;40mPassword >> \033[0;37;40m >>") != "1bd0":
	print("\033[1;31;40m =====PASSWORD WRONG===== \033[0;37;40m".center(75))
	time.sleep(0.3)
	os.system("clear")
	
	
else:
	print("\033[1;35;33m =====PASSWORD CORRECT===== \033[0;37;40m".center(75))
	time.sleep(0.5)
	os.system("clear")
print("welcome \033[1;35;40m")
h = {
"abderrahman" : "Name : Abderrahman \nF.name : Sakit \nAge :?? \nBirthday :??/??/????  "
} 
f = str(input("print a name \033[1;32;40m  : "))
#while input("print a \033[1;32;40m name : \033[0;37;40m") != h:
	#print("THIS NAME DO NOT EXIST")
#else :
#	print("Found")
#	
def restart_program():

   python = sys.executable

   os.execl(python, python, * sys.argv)

   curdir = os.getcwd()
try:
	print(  "\033[0;37;40m" +h[f] )
except:
	print("Not Found")
	restart_program()
#	restart_program()
	
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
	

	

	
