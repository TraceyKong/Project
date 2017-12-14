from flask import Flask, redirect, render_template, request
import project as p
import extended_part1 as e1

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/input",methods=["POST","GET"])
def index():
	md = p.mock_data[1:]
	if request.method=="GET":
		return render_template("inverted_index.html",result = md, lresult = str(len(md))+'/'+str(len(md))+' results')
	term = request.form['term']
	if not term.strip(): return render_template("inverted_index.html",nresult = "No result for '"+term+"' please enter again.",lresult = '0/'+str(len(md))+' results')
	t = p.clean_text(term).title().split()
	result = []
	if len(term)>1:
		for i in t:
			if not p.valid_key(i): 
				return render_template("inverted_index.html",
					nresult = "No result for '"+term+"', please enter again.")
			result = e1.and_query_1(result,i)
		result = p.return_values(result)
		return render_template("inverted_index.html",result = result, lresult = str(len(result))+'/'+str(len(md))+' results')
	elif p.valid_key(t[0]):
		return render_template("inverted_index.html",result = p.return_values(p.mock_data_dic[t[0]]))
 	return render_template("inverted_index.html",nresult = "No result for '"+term+"', please enter again.",lresult = '0/'+str(len(md))+' results')

@app.route("/input/narrow_search",methods=["POST","GET"])
def narrow():
	md = p.mock_data[1:]
	if request.method=="GET":
		return render_template("narrow_search.html",result = md, lresult = str(len(md))+'/'+str(len(md))+' results')
	term = request.form['term']
	if not term.strip(): return render_template("inverted_index.html",nresult = "No result for '"+term+"' please enter again.",lresult = '0/'+str(len(md))+' results')
	t = p.clean_text(term).title().split()
	result = []
	if len(term)>1:
		for i in t:
			if not p.valid_key(i): 
				return render_template("inverted_index.html",
					nresult = "No result for '"+term+"', please enter again.")
			result = e1.and_query_1(result,i)
		result = p.return_values(result)
		return render_template("inverted_index.html",result = result, lresult = str(len(result))+'/'+str(len(md))+' results')
	elif p.valid_key(t[0]):
		return render_template("inverted_index.html",result = p.return_values(p.mock_data_dic[t[0]]))
 	return render_template("inverted_index.html",nresult = "No result for '"+term+"', please enter again.",lresult = '0/'+str(len(md))+' results')
app.run(debug=True,host="0.0.0.0",port=5000)
