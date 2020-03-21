from flask import Flask,render_template,request, session
#from cachelib.file import FileSystemCache
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"]= "filesystem"
Session(app)


@app.route("/",methods=["GET","POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html",notes=session["notes"])


@app.route("/hello",methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return"Please Submit form instead"
    else:
        name = request.form.get("name")
        return render_template("hello.html",name=name)

@app.route("/more")
def more():
    ##names=["ALice","Bob","Charlie","deepa"]
    return render_template("more.html")
