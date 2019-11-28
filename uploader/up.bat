# create the documentation
Readme.md functions meta, description and example

# update the repository
git add .
git commit -m "message"
git push -u origin master

# make a release with name, tag, description and get link

# update version name, download link at setup.py

python setup.py sdist
twine upload dist/* -u username -p password

pip install --upgrade shaonutil