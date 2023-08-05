from flask import Flask, render_template, request
import ibm_db

app = Flask(__name__, template_folder="templates/")

Flask (__name__)

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30756;UID=tqy10628;PWD=cqy6wVyy6d6z8DkS;SECURITY=SSL;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt", "", "")
print(ibm_db.active(conn))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
       uname = request.form['username']
       pword = request.form['password']
       print(uname, pword)
       sql = 'SELECT * FROM REGISTER_FDP WHERE USERNAME = ? AND PASSWORD = ?'
       stmt =ibm_db.prepare(conn , sql)
       ibm_db.bind_param(stmt, 1,  uname)
       ibm_db.bind_param(stmt, 2,  pword)
       ibm_db.execute(stmt)
       out = ibm_db.fetch_assoc(stmt)
       print(out)    
       if out:
           role=out['ROLE']
           if role == "0":
               return render_template("admninprofile.html")
           elif role == 1:
               return render_template("studentprofile.html")
           else:
               return render_template("facultyprofile.html")
           
       else:
        msg = "Invalid Credentials"
        return render_template("login.html", login_message = msg)
           
            
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug = True)