from pm import PasswordManager

pm = PasswordManager()

def main():

	print("""
	▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
	▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
	▓▓░░░░░░░░░░░▓▓▓░▓░░░░░▓░▓▓░░░░░░░░░░░░░▓▓
	▓▓░░░░░░░░░░░▓░▓░░▓░▓░▓░░▓░▓░░▓▓▓░░░░░░░▓▓
	▓▓░░░░░░░░░░░▓░░░░░▓░▓░░░▓▓░░░░░░░░░░░░░▓▓
	▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
	▓▓░░░░░▓▓░░░░▓▓▓▓▓▓░░▓▓▓▓░░▓▓░░░░▓▓░░░░░▓▓
	▓▓░░░░░▓▓░░░░▓▓░░▓▓░░▓▓░░░░▓▓░░▓▓░░░░░░░▓▓
	▓▓░░░░░▓▓░░░░▓▓░░▓▓░░▓▓░░░░▓▓▓▓░░░░░░░░░▓▓
	▓▓░░░░░▓▓░░░░▓▓░░▓▓░░▓▓░░░░▓▓░░▓▓░░░░░░░▓▓
	▓▓░░░░░▓▓▓▓░░▓▓▓▓▓▓░░▓▓▓▓░░▓▓░░░░▓▓░░░░░▓▓
	▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
	▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
	_______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
	______▒_______________▒▒▒▒▒▒▒▒
	_____▒________________▒▒▒▒▒▒▒▒
	____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
	___▒
	__▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
	_▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
	▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
	▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
	▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
	▒▒

	--------------------------------------------------------------
	 Welcome to Password-Lock, your secure password Manager !            
	--------------------------------------------------------------

	 Choose an action below to begin:

	 ##  NOTE: If you Want to store your keys or password       ##
	 ##  seperated, you have to transfer it back in the key or  ##
	 ##  password file used by Password-Lock before starting    ##
	 ##  the program.                                           ##

	--------------------------------------------------------------

	 (1) Create a new key
	 (2) Load an exiting key
	 (3) Create a new password file
	 (4) Load an existing password file
	 
	 (s) Show passwords
	 (a) Add data
	 (c) Change password or username
	 (g) Generate an random password
	 (q) SAVE

	""")

	done = False
	while not done:
		choice = input("Enter your Choice: ")

		if choice == "1":
			path = input("Enter an filename to create an key file: ")
			pm.create_key(path)
		if choice == "2":
			path = input("Enter the filename to load the key: ")
			pm.load_key(path)
		if choice == "3":
			path = input("Enter an filename to create a password file: ")
			pm.generate_password_file(path)
		if choice == "4":
			path = input("Enter an filename to load an exiting password file: ")
			pm.load_password_file(path)
		
		if choice == "a":
			page = input("software: ")
			user = input("username or email: ")
			pwd = input("password: ")
			pm.add_password(page, user, pwd)
		if choice == "s":
			pm.show_table()
		if choice == "c":
			page = input("software you want to change: ")
			new_user = input("username: ")
			new_pwd = input("password: ")
			new_data = [new_user, new_pwd]
			pm.change_pwd(page, new_data)
		if choice == "g":
			lenght = int(input("password lenght: "))
			pm.generate_password(lenght)
		if choice == "q":
			pm.save()
			done = True


if __name__ == '__main__':
	main()
