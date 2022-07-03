import random
import string
import base64
from cryptography.fernet import Fernet
from rich.table import Table
from rich.console import Console


class PasswordManager:

	def __init__(self, keyLen = 32):
		self.keyLen = keyLen
		self.key = ""
		self.pfile = ""
		self.kfile = ""
		self.decDa = b''
		self.data = b''

	def create_key(self, path):
		self.key = base64.b64encode((''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(self.keyLen))).encode('ascii'))
		with open(path, "wb") as f:
			f.write(self.key)
			

	def load_key(self, path):
		try:
			with open(path, "rb") as f:
				self.key = f.read()
		except FileNotFoundError:
			red = "#d13c0f"
			console = Console()
			console.print("Error! File not Found! Please enter an valid filename!", style=red)
	
	def generate_password_file(self, path):
		with open(path, "wb") as f:
			pass

	def load_password_file(self, path):
		self.pfile = path
		try:
			with open(self.pfile, "rb") as f:
				self.data = f.read()
		except FileNotFoundError:
			red = "#d13c0f"
			console = Console()
			console.print("Error! File not Found! Please enter an valid filename!", style=red)
			
		if len(self.data) > 0:
			self.decrypt()

	def show_table(self):
		table = Table()

		table.add_column("Page")
		table.add_column("Username")
		table.add_column("Password", style="cyan")

		for line in (self.decDa.decode()).splitlines():
			self.page, self.user, self.pwd = line.split(";")

			#loops over every line and adds it to the table
			table.add_row(self.page, self.user, self.pwd)

		print("\n" * 10)
		console = Console()
		console.print(table, justify="left")
		print("\n" * 2)
		
	def change_pwd(self, wpage, newdata): #wpage == wanted page
		g = ""
		
		#get every entry in forloop and change if its the wanted
		for l in (self.decDa.decode()).splitlines():
			page, user, pwd = l.split(";")
			user = newdata[0] if (page==wpage) else user
			pwd = newdata[1] if (page==wpage) else pwd
			g += f"{page};{user};{pwd}\n"
		
		#encode the data and put it in decoded data // Note: name changed decoded data has to be decoded xD
		g_enc =g.encode()
		self.decDa = g_enc

	def add_password(self, page, user, password):
		self.decDa += (f"{page};{user};{password}\n").encode()

	def encrypt(self):
		f = Fernet(self.key)
		self.data = f.encrypt(self.decDa)

	def decrypt(self):
		f = Fernet(self.key)
		self.decDa = f.decrypt(self.data)

	def save(self):
		try:
			self.encrypt()
			with open(self.pfile, "wb") as f:
				f.write(self.data)
		except ValueError:
			red = "#d13c0f"
			console = Console()
			console.print("NOTE: NO DATA ADDED OR LOADED", style=red)

	def generate_password(self, lenght):
		#generate a password with given lenght
		chars = string.ascii_letters + string.digits + "!#$%&'()*+, -./:;<=>?@[]^_`{|}~"
		gen_pwd = "".join(random.choice(chars) for i in range(lenght))
		print(f"Your generated password is: {gen_pwd}")
		