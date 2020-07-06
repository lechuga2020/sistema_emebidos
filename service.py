from flask import Flask
from flask import Response
from flask import render_template
from flask import request, redirect, url_for, send_from_directory
from datetime import datetime
import io

import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
import csv
from datetime import datetime
from io import StringIO
from flask import Flask, stream_with_context
from werkzeug.datastructures import Headers
from werkzeug.wrappers import Response
from flask import send_file

UPLOAD_FOLDER = os.path.abspath(os.getcwd())

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def root():
    
    return "hello, World!"

@app.route('/filtro')
def filtro():
    archivo = open("coeff.txt", 'r')
    A_coeff = np.genfromtxt('coeff.txt', dtype='double')
    archivo.close()
    archivo = open("X_signal.txt", 'r')
    x_i = np.genfromtxt('X_signal.txt', dtype='double')

    archivo.close()
    n = len(A_coeff);

    n = n-1;
    k = len(x_i)-1;
    y = np.zeros(k+1);
    for k in range(k,-1,-1):
        y[k] = FIR(k,n,A_coeff,x_i)

    print(y)
    y_file = np.savetxt('y.txt', y, fmt="%e")


    return plot_png(x_i,y)
    #return downloadFile()
    
def FIR(k,n,a_coeff, x):

	if n < 0:
		return 0;
	else:
		a_n = a_coeff[n];
		multp = 0;
	if k-n <0:
		multp = 0;
	else:
		x_i = x[k-n];
		multp = a_n*x_i;
	#suma = y + multp;
	n = n-1
	y = multp + FIR(k, n, a_coeff, x);
	print(k)
	return y

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "/home/aldo/proyecto/sistema_emebidos/y.txt"
    return send_file(path, as_attachment=True)


#@app.route('/plot.png')
def plot_png(x,y):
    fig = create_figure(x,y)
    output = io.BytesIO()
   
    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype='image/png')
def create_figure(x,y):
	with open('register.dat') as file:
		file_data = file.readlines()
	# create figure
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.plot(x)    
	axis.plot(y)

	return fig 

if __name__=="__main__":
    app.run()
