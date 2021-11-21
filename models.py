from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import session
from flask import Flask


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0000@localhost/News'    
db = SQLAlchemy(app)

""" News Model """

class News(db.Model):
    __tablename__ = 'News'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    overview = db.Column('overview', db.String)
    link = db.Column('link', db.String)
    paragraphs = db.Column('paragraphs', db.Text)
    summary = db.Column('summary', db.Text)


    def __init__(self, id, title, overview, link, paragraphs, summary):
        self.id = id
        self.title = title
        self.overview = overview
        self.link = link
        self.paragraphs = paragraphs
        self.summary = summary
 

    
    
    def find_id():
        news = News.query.all()
        return len(news)

        
def add_news_to_db(new_title, new_overview, new_link, new_paragraphs, summary):
        
        news = News(News.find_id()+1, new_title, new_overview, new_link, new_paragraphs, summary)
        db.session.add(news)
        db.session.commit()

def get_the_news():
        news = News.query.all()   
        news = news[-10:]
        return news
        

# db.create_all()

class User(db.Model):
    """User model"""
    __tablename__ = 'Users'



    id = db.Column('id', db.Integer, primary_key=True)



    login = db.Column('login', db.String(50))



    password = db.Column('password', db.String(50))



    token = db.Column('token', db.String(255))



    def __init__(self,id,login, password, token):



        self.id = id

        self.login = login

        self.password = password

        self.token = token


    
    def verify(loginAttempt, passwordAttempt):
        loginQuery = User.query.filter_by(login=loginAttempt).first()
        if loginQuery != None and loginQuery.password == passwordAttempt:
            return True
        else: False
    
    def verifyToken(Token):
        loginQuery = User.query.filter_by(token=Token).first()
        if loginQuery != None:
            return True
        else: False

    def saveToken(loginAttempt, Token):
        loginQuery = User.query.filter_by(login=loginAttempt).first()
        loginQuery.token = Token
    
        db.session.commit()

# db.create_all() 
""" Use this command to implement the database 1 time"""

# print(News.find_id())
# News.add_news_to_db("cordana to the moon", 'Cordanatothemoon', 'mooon', 'dsadasdadada')

    