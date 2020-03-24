"""Process"""
import mysql.connector as mysql
import os
import subprocess
import time

"""
To Resolve mysql problems:
go to mysql folder > aria_chk -r
delete araia_log.### files in mysql data folder
change the port=3306 to anything else in line 20,28 in my.ini in mysql data folder
if anything didn't recover then, go to mysqsl/backup, copy everything and go to mysql/data folder , delete everything and past here.
"""

def start_mysql_server(mysql_bin_folder,mysql_config_file):
	"""Start mysql server"""
	DETACHED_PROCESS = 0x00000008	
	return subprocess.Popen([os.path.join(mysql_bin_folder,"mysqld.exe"),"--defaults-file="+mysql_config_file,"--standalone"],creationflags=DETACHED_PROCESS)

def remove_aria_log(mysql_data_dir):
	"""Removing aria_log.### files to in mysql data dir to restart mysql"""
	aria_log_files = [file for file in os.listdir(mysql_data_dir) if 'aria_log.' in file]
	for aria_log in aria_log_files:
		aria_log = os.path.join(mysql_data_dir,aria_log)
		os.remove(aria_log)

def get_mysql_datadir(mysql_bin_folder,user,pass_=''):
	"""Get mysql data directory"""
	process = subprocess.Popen([os.path.join(mysql_bin_folder,"mysql"),"--user="+user,"--password="+pass_,"-e","select @@datadir;"],stdout=subprocess.PIPE)
	out, err = process.communicate()
	out = [line for line in out.decode('utf8').replace("\r\n","\n").split('\n') if line != ''][-1]
	datadir = out.replace('\\\\','\\')
	return datadir


#myNowMYSQL = MySQL(config._sections['DB_INITIALIZE'])
#{'host': 'localhost', 'user': 'root', 'password': ''}

#myNowMYSQL.config = config._sections['DB_AUTHENTICATION']
class MySQL:
	def __init__(self,config,log=False):
		self.log = log
		self._config = config
		self.filter_config()
		self.make_cursor()

	def __del__(self):
	    self._cursor.close()
	    self.mySQLConnection.close()

	@property
	def config(self):
		return self._config
		
	@config.setter
	def config(self, new_value):
		self._config = new_value
		self.filter_config()
		self.make_cursor()
	
	def filter_config(self):
		mustList = ['host','user','password']
		for key in self._config:
			if not key in mustList:
				ValueError(key,"should have in passed configuration")
				break

	def make_cursor(self):
		try:
			# Connection parameters and access credentials
			if 'database' in self._config:
				mySQLConnection = mysql.connect(
					host = self._config['host'],
					user = self._config['user'],
					passwd = self._config['password'],
					database = self._config['database']
				)
			else:
				print('this')
				mySQLConnection = mysql.connect(
					host = self._config['host'],
					user = self._config['user'],
					passwd = self._config['password']
				)
			self.mySQLConnection = mySQLConnection

		except mysql.errors.OperationalError:
			print("Error")
			# shaonutil.process.remove_aria_log('C:\\xampp\\mysql\\data')

		self._cursor = mySQLConnection.cursor()

	def is_mysql_user_exist(self,mysql_username):
		mySQLCursor = self._cursor
		mySqlListUsers = "select host, user from mysql.user;"
		mySQLCursor.execute(mySqlListUsers)
		userList = mySQLCursor.fetchall()
		foundUser = [user_ for host_,user_ in userList if user_ == mysql_username]
		if len(foundUser) == 0:
			return False
		else:
			return True

	def listMySQLUsers(self):
		"""list all mysql users"""
		mySQLCursor = self._cursor
		mySqlListUsers = "select host, user from mysql.user;"
		mySQLCursor.execute(mySqlListUsers)
		userList = mySQLCursor.fetchall()
		print("List of users:")
		for user in userList:
		    host_,user_ = user
		    print(host_,user_)


	def createMySQLUser(self, host, userName, password,
	               querynum=0, 
	               updatenum=0, 
	               connection_num=0):
		cursor = self._cursor
		try:
			print("MySQL > Creating user",userName)
			sqlCreateUser = "CREATE USER '%s'@'%s' IDENTIFIED BY '%s';"%(userName,host,password)
			cursor.execute(sqlCreateUser)
		except Exception as Ex:
			print("Error creating MySQL User: %s"%(Ex));

	def grantMySQLUserAllPrivileges(self, host, userName,
	               querynum=0, 
	               updatenum=0, 
	               connection_num=0):
		cursor = self._cursor
		try:
			print("MySQL > Granting all PRIVILEGES to user",userName)
			sqlGrantPrivilage = "GRANT ALL PRIVILEGES ON * . * TO '%s'@'%s';"%(userName,host)
			cursor.execute(sqlGrantPrivilage)
			cursor.execute("FLUSH PRIVILEGES;")

		except Exception as Ex:
			print("Error creating MySQL User: %s"%(Ex));

	def is_db_exist(self,dbname):
		cursor = self._cursor

		cursor.execute("SHOW DATABASES")
		databases = cursor.fetchall()
		databases = [x[0] for x in databases]
		if dbname not in databases:
			return False
		else:
			return True

	def create_db(self,dbname):
		cursor = self._cursor
		print("Creating database "+dbname+" ...")
		cursor.execute("CREATE DATABASE "+dbname)

	def is_table_exist(self,tbname):
		cursor = self._cursor
		cursor.execute('SHOW TABLES')
		tables = cursor.fetchall()
		tables = [ x[0] for x in tables ]
		if tbname in tables:
			return True
		else:
			return False

	def create_table(self,tbname,column_info):
		cursor = self._cursor
		print("Creating table "+tbname+" ...")
		cursor.execute("CREATE TABLE "+tbname+" (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,"+''.join([' '+info+' '+column_info[info]+',' for info in column_info])[:-1]+")")


def get_unique_id_from_field(config,key_length,field_name):
	
	db = mysql.connect(
		host = config['host'],
		user = config['user'],
		passwd = config['password'],
		database = config['database']
	)
	
	table = config['table']

	cursor = db.cursor()

	sid = generateCryptographicallySecureRandomString(key_length)
	
	while True:
		query = "SELECT * FROM "+table+" WHERE `"+field_name+"` = '"+sid+"'"

		## getting records from the table
		cursor.execute(query)

		## fetching all records from the 'cursor' object
		records = cursor.fetchall()

		## Showing the data
		for record in records:
		    print(record)


		if(len(records)>1):
			print("matched with previously stored sid")
			sid = generateCryptographicallySecureRandomString(key_length)
		else:
			print("Got unique sid")
			break
			
	return sid