# Coursework:Google doodle site structure

import os
from flask import Flask, redirect, url_for, abort,render_template, send_from_directory
from glob import iglob
from os.path import basename
app = Flask(__name__)

#this is the base Design across the web app
def design():
  return render_template ('standard.html')

#This gets all the still doodles to be used across the web app
def jpgs():
   images = os.listdir('./static/all_doodles/still_doodles')
   print(images)
   return render_template ('imageload.html', images=images)

#this is the homepage of the app
@app.route("/")
def root():
  images = os.listdir('./static/all_doodles/still_doodles')
  print(images)
  return render_template ('newhome.html',images=images)


#this lists all available doodles
@app.route("/all-doodles/")
def alldoodles():
   images = os.listdir('./static/all_doodles/still_doodles')
   print(images)
   return render_template ('imageload.html', images=images)

@app.route("/latest-doodle/")
def newdoodle():
   return render_template ('home.html')


@app.route("/test")
def testing():
   return render_template ('test.html')



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

