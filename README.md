# Embedded systems
Final project of embedded systems

## Abstract project

The aim of this project is to apply knowledge of git_hub, linux, python and signal processing. That's why the project consists of a python web service of the appi Flask for low-pass filtering of a signal with 4000 Hz cutoff frequency. The web service simulates the data collection of an AD by reading a txt file, and by reading a text file containing the pass filter coefficients it will perform the signal filtering.  The result for the user is a data file of the filtered signal and a comparison chart of the before and after filtering

## Steps to install python web service: 


sudo apt install python3-pip

pip3 install virtualenv

virtualenv -p python3 .venv 

source .venv/bin/activate

pip install -r requirements.txt

pip intall flask

FLASK_APP=service.py flask run 


## Linuxs command to enter to virtual env. and run flask: 


source .venv/bin/activate

FLASK_APP=service.py flask run

## GIt-Hub content

* Coeff.txt: It is a text file that contains in a single column, the coefficients of the low-pass filter.

* X_signal.txt:  It is a text file containing the samples of a voice signal mixed with several other signals with frequencies higher than 4000Hz. This will be the signal to be filtered, the user can modify this file or put his own.  


