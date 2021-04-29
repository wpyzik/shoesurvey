from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from werkzeug import secure_filename

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgres://akezcdllpanpyq:80a8d64c47a482d3aa77e616047fd535a9dec0979ca6952f070b1611a0f15f2a@ec2-52-6-143-153.compute-1.amazonaws.com:5432/dc5ei6gj8fe59g?sslmode=require"
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    shoe=db.Column(db.Integer)

    def __init__(self, email, shoe):
        self.email=email
        self.shoe=shoe

@app.route ("/")
def index():
    return render_template ("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        file=request.files["file"]
        #content=file.read()
        file.save(secure_filename("Uploaded"+file.filename))
        with open("Uploaded"+file.filename,"a") as f:
            f.write("It was added later")
            return render_template("index.html", btn="download.html")
    return render_template("index.html", text="It looks like we already have data from this email address")


@app.route("/download")
def download():
    return send_file("Uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":  #meaning- if script is executed, not imported we will execute those lines
    app.debug=True
    app.run() #we will run the app
