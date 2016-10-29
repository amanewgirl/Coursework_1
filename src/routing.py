# Coursework:Google doodle site structure

from flask import Flask, redirect, url_for, abort,render_template
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
   jpgfile = Image.open("static/all_doodles/still_doodles/10_October.jpg")
   return render_template ('test.html', jpgfile = jpgfile)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

