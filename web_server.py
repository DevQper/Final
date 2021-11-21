from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response, url_for
from flask import request
from flask.json import jsonify
from flask.templating import render_template
import jwt
from werkzeug.utils import redirect
from services import PutResults
from coin_market_news import news_scraper
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session
from models import User

from services import GetResults

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0000@localhost/News'    
db = SQLAlchemy(app)


""" Start of the controller blocks """

@app.route('/coin', methods=['POST', 'GET'])
def coin():
    if request.method == "POST":
         result = request.form["cryptoname"]
         return redirect(url_for("result", cryptoname=result))
    else:
        return render_template('index.html')

@app.route('/<cryptoname>')
def result(cryptoname):
    PutResults(cryptoname)
    result = GetResults()
    for news in result:
        print(news.title)
    return render_template('result_page.html', content = result)

@app.route('/login')
def login():

    auth = request.authorization
    if auth:
        if User.verify(auth.username, auth.password):
            token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
            User.saveToken(auth.username, token)
            return jsonify({'token': token, 'Login': auth.username})
        else:
            return '<h1> : Could not found a user with login: <login> </h1>'
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


@app.route('/protected', methods=['GET', 'POST'])
def protected():
    token = request.args.get('token')
    if User.verifyToken(token):
        return '<h1>Hello, token which is provided is correct </h1>'
    else:
        return '<h1>Hello, Could not verify the token </h1>'    




if __name__ == '__main__':
    app.run(debug=True)


    