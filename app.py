from flask import Flask, redirect, render_template, request
import project

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/input",methods=["POST","GET"])
def index():
	if request.method=="GET":
		return render_template("inverted_index.html")
	term = request.form['term']
	if project.valid_key(term):
 		return render_template("inverted_index.html",term = project.return_values("MOCK_DATA.csv",term))
 	else: return render_template("inverted_index.html",term = "No result, please enter again")

app.run(debug=True,host="0.0.0.0",port=5000)
