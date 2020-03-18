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
	
	

def changing_version_name(new_vname):
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
	

if __name__ == '__main__':
	print("Showing Previous Version :",get_version_name())
	new_vname = input("Give    New Version Name : ")
	changing_version_name(new_vname)
	

	cleaning_before_commit()

	commit_msg = input("Give Commit Message : ")

#git diff-index --quiet HEAD || git commit -m "mesage";
#tested
	if platform.system() == 'Linux':
		commands = """git add .
git diff-index --quiet HEAD || git commit -m \""""+commit_msg+"""\";
git push -u origin master
pip3 uninstall """+package_name+""" -y
python3 setup.py sdist bdist_wheel
python3 setup.py install"""
	elif platform.system() == 'Windows':
		commands = """git add .
git diff-index --quiet HEAD || git commit -m \""""+commit_msg+"""\";
git push -u origin master
pip3 uninstall """+package_name+""" -y
python setup.py sdist bdist_wheel
python setup.py install"""

	commands = commands.split("\n")

	for command in commands:
		for path in execute_shell(command):
		    print(path, end="")

	cleaning_before_commit()