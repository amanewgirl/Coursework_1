# Coursework:Google doodle site structure

import os
from flask import Flask, redirect, url_for, abort,render_template, send_from_directory
from glob import iglob
from os.path import basename
app = Flask(__name__)

#this is the base Design across the web app
def design():
  return render_template ('standard.html')

#this is the homepage of the app
@app.route("/")
def root():
  return render_template ('home.html')


#this lists all available doodles
@app.route("/all-doodles/")
def alldoodles():
    return render_template ('all.html')



@app.route("/test")
def testing():
   return render_template ('test.html')


@app.route("/test2")
def tests():
    jpgs = iglog('static/all_doodles/still_doodles/*.jpg')                  # An iterator of 'img/1.png', 'img/2.png', ...
    jpgs = (basename(jpg) for jpg in jpgs)
    return render_template ('test2.html', jpgs=jpgs)


@app.route("/test3")
def testingagain():
   images = os.listdir('./static/all_doodles/still_doodles')
   print(images)
   return render_template ('test3.html', images=images)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

