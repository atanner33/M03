from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


#model - python-ey version of a db table. Through classes
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.publisher}"

#route says when you go to this url..perform this function.
@app.route('/')
def index():
    return 'Hello'

#create a route that when it is visited, it displays all of the books in the database
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []

    for book in books:
        book_data = {'Book Title:': book.title, 'Author:': book.author, 'Publisher:': book.publisher}
        output.append(book_data)
    return {"books": output}