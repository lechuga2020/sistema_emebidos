# Embedded systems
Final project of embedded systems  

steps to install python web service: 

sudo apt install python3-pip
pip3 install virtualenv
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
pip intall flask
FLASK_APP=service.py flask run
