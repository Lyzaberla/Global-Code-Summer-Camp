#this imports all the objects in the flask library
from flask import * 
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', items = items)

items = []

@app.route('/add_todo')
def add_todo():
	item = request.args.get("item")
	items.append(item)
	return redirect("http://localhost:5000/", code=302)

#for json get files
@app.route('/get_todos')
def get_todos():
	resp = Response(json.dumps(items))
	resp.headers['Content-Type'] = 'application/json'
	return resp

#handles app properties (something like that)
if __name__ == '__main__':
#this side is for the heroku side
	port = os.environ.get('PORT', 5000)
app.run(debug=True, host='0.0.0.0', port=port)
