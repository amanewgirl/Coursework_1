# Coursework:Google doodle site structure

import os
from flask import Flask, redirect, url_for, abort,render_template, send_from_directory, request
from os.path import basename
app = Flask(__name__)

#this is the base Design across the web app
def design():
  return render_template ('standard.html')


#this is the homepage of the app
@app.route("/")
def root():
    images = os.listdir('./static/all_doodles/still_doodles')
    return render_template ('home.html',images=images)


#this lists all available doodles and returns more categories if signed in
@app.route("/all-doodles/")
@app.route("/all-doodles/<name>")
def alldoodles(name=None):

#Opens the directory for jpgs
    pathstill = "./static/all_doodles/still_doodles"
    images = os.listdir(pathstill)

    for file in images:
      print file

#Opens the directory for gifs
    pathgifs = "./static/all_doodles/gifs"
    gifs = os.listdir(pathgifs)

    for file in gifs:
      print file

    return render_template ('imageload.html', images=images, name=name, gifs=gifs)



#The latest doodle from Google is shown here
@app.route("/latest-doodle/")
def newdoodle():
   return render_template ('latest.html')


#Allows temporary sign in to access hidden categories
@app.route('/account')
def account():
   return render_template('account.html')

@app.route("/signedin", methods = ['POST', 'GET'])
def signedin():
   if request.method == 'POST':
      signedin = request.form 
      return render_template("sign.html",signedin = signedin)


#Allows single picture uploads for signed in  user
@app.route('/upload')
def upload():
   return render_template('upload.html')

@app . route ("/uploading", methods =[ 'POST','GET'])
def uploading():
  if request . method == 'POST':
  	f = request.files ['file']
	f.save ('static/uploads/upload.png')
        return " File Uploaded "
 






if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

