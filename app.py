from flask import Flask, redirect, render_template, request
import project

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/input",methods=["POST","GET"])
def index():
	if request.method=="GET":
		return render_template("inverted_index.html",result = project.mock_data[1:])
	term = request.form['term']
	if project.valid_key(term):
		return render_template("inverted_index.html",result = 
			project.return_values(project.mock_data_dic[term]))
 	else: return render_template("inverted_index.html",nresult = "No result, please enter again")

app.run(debug=True,host="0.0.0.0",port=5000)
