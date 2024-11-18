from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)



class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Colunm(db.String(120),unique =True, nullable=False)

    def __repr__(self):
        return f"{self.name} - {self.description}"
@app.route('/')
def index():
    return 'Hello!'


@app.route('/books')
def get_books():
    books = Books.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'description': book.description}

        output.append(book_data)

    return {"books": output}


@app.route('/books/<id>')
def get_books(id):
    book = Books.query.get_or_404(id)
    return {"name": book.name, "description": book.description}


@app.route('/books', methods=['POST'])
def add_books():
    book = Books(name=request.json['name'],
                  description=request.json['description'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Books.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!@"}