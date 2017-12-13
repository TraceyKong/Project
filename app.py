from flask import Flask, redirect, render_template, request
import project as p
import extended_part1 as e1

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/input",methods=["POST","GET"])
def index():
	if request.method=="GET":
		return render_template("inverted_index.html",result = p.mock_data[1:])
	term = request.form['term']
	if term=='': return render_template("inverted_index.html",result = p.mock_data[1:])
	t = p.clean_text(term).title().split()
	result = []
	if len(term)>1:
		for i in t:
			if not p.valid_key(i): 
				return render_template("inverted_index.html",
					nresult = "No result for '"+term+"', please enter again.")
			result = e1.and_query_1(result,i)
		return render_template("inverted_index.html",result = p.return_values(result))
	elif p.valid_key(t[0]):
		return render_template("inverted_index.html",result = p.return_values(p.mock_data_dic[t[0]]))
 	return render_template("inverted_index.html",nresult = "No result for '"+term+"', please enter again.")

app.run(debug=True,host="0.0.0.0",port=5000)
