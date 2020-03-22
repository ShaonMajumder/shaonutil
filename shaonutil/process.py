"""Process"""
import os
import subprocess

def start_mysql_server(mysql_bin_folder,mysql_config_file):
	"""Start mysql server"""
	DETACHED_PROCESS = 0x00000008	
	return subprocess.Popen([os.path.join(mysql_bin_folder,"mysqld.exe"),"--defaults-file="+mysql_config_file,"--standalone"],creationflags=DETACHED_PROCESS)

def get_mysql_datadir(mysql_bin_folder,user,pass_=''):
	"""Get mysql data directory"""
	
	process = subprocess.Popen([os.path.join(mysql_bin_folder,"mysql"),"--user="+user,"--password="+pass_,"-e","select @@datadir;"],stdout=subprocess.PIPE)
	out, err = process.communicate()
	out = [line for line in out.decode('utf8').replace("\r\n","\n").split('\n') if line != ''][-1]
	datadir = out.replace('\\\\','\\')
	return datadir