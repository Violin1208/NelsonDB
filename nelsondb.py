from flask import Flask
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nelson:debl@localhost/nelson'

 
from views import *
 
if __name__ == '__main__':
    app.run()