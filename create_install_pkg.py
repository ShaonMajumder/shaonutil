import os
import time
import shutil
import platform
import subprocess
import shaonutil

package_name = 'shaonutil'

def execute_shell(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def cleaning_before_commit():
	files= package_name+""".egg-info
build
dist
.eggs
"""
	print("Cleaning files -",files)

	files = files.split('\n')

	for file in files:
		if os.path.exists(file):
			try:
				shutil.rmtree(file)
			except:
				os.remove(file)

def get_version_name():
	lines = shaonutil.file.read_file('setup.py')
	i = 0
	for line in lines:
		if '__version__' in line:
			marker = '\''
			s = line
			start = s.find(marker) + len(marker)
			end = s.find(marker, start)
			vname = s[start:end]
			break
		i+=1
	return vname
	
	

def changing_version_name(prev_vname,new_vname):
	lines = shaonutil.file.read_file('setup.py')

	strs ='\n'.join(lines)
	strs = strs.replace(prev_vname,new_vname)
	shaonutil.file.write_file('setup.py',strs)

def changing_version_name_prev(new_vname):
	lines = shaonutil.file.read_file('setup.py')

	i = 0
	for line in lines:
		if '__version__' in line:
			marker = '\''
			s = line
			start = s.find(marker) + len(marker)
			end = s.find(marker, start)
			vname = s[start:end]
			s = s.replace(vname,new_vname)
			break
		i+=1
	
	lines[i] = s
	strs = '\n'.join(lines)
	shaonutil.file.write_file('setup.py',strs)
	
def make_config():
	"""
	package_name
	initial_version
	#0.0.0.0.1
	author
	author_email
	git_project_url
	download_url
	keywords
	"""
	pass




def checks_folder():
	print("Checking the required files/folders ...")
	folders = """README.md
requirements.txt
.git
LICENSE
setup.py"""

	folders = folders.split('\n')
	for folder in folders:
		if not os.path.exists(folder):
			print("Warning :",folder,"does not exist.")


def check_modules():
	print("Checking the required modules ...")
	modules = """setuptools
wheel
twine
pipreqs"""
	modules = modules.split('\n')
	
	for module in modules:
		found = shaonutil.file.package_exists(module)
		if not found:
			print(module," package is not installed.")
			print(module," package is installing.")

			if platform.system() == 'Linux':
				command = """pip3 install """+module
			elif platform.system() == 'Windows':
				command = """pip3 install """+module

			for path in execute_shell(command):
			    print(path, end="")


def commit_push():
	commit_msg = input("Give Commit Message : ")

	if platform.system() == 'Linux':
		commands = """git add .
git commit -m \""""+commit_msg+"""\";
git push -u origin master"""
	elif platform.system() == 'Windows':
		commands = """git add .
git commit -m \""""+commit_msg+"""\";
git push -u origin master"""

	commands = commands.split("\n")

	for command in commands:
		for path in execute_shell(command):
		    print(path, end="")


if __name__ == '__main__':
	check_modules()
	checks_folder()



	pre_vname = get_version_name()
	print("Showing Previous Version :",pre_vname)
	new_vname = input("Give    New Version Name : ")
	changing_version_name(pre_vname,new_vname)
	

	cleaning_before_commit()
	commit_push()
	quit()

	pypi_user = input("Give pypi user : ")
	pypi_pass = input("Give pypi pass : ")

	### git diff-index --quiet HEAD || git commit -m \""""+commit_msg+"""\";

	if platform.system() == 'Linux':
		commands = """pip3 uninstall """+package_name+""" -y
python3 setup.py sdist bdist_wheel
twine upload dist/* --user="""+pypi_user+""" --pass="""+pypi_pass+"""
python3 setup.py install"""
	elif platform.system() == 'Windows':
		commands = """pip3 uninstall """+package_name+""" -y
python setup.py sdist bdist_wheel
twine upload dist/* --user="""+pypi_user+""" --pass="""+pypi_pass+"""
python setup.py install"""



	commands = commands.split("\n")

	for command in commands:
		for path in execute_shell(command):
		    print(path, end="")

	cleaning_before_commit()


	