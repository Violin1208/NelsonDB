from nelsondb import app
from flask import render_template, request
from models import Nelson
 
@app.route('/')
def index():
	return render_template(
       'list.html',
       letters=Nelson.query.all())

@app.route('/letter/<int:id>')
def letter(id):
	return render_template(
       'single.html',
       letter=Nelson.query.filter_by(id=id).one())
