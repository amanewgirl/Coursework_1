# Coursework:Google doodle site structure

from flask import Flask, redirect, url_for, abort,render_template
app = Flask(__name__)

def design():
  return render_template ('standard.html')

@app.route("/")
def root():
  return render_template ('home.html')
 
@app.route("/Search-a-doodle/")
def hello():
  return "If you want to search for doodles, you've found the right place"

@app.route("/more-doodles")
def goodbye():
  return "View all doodles"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

