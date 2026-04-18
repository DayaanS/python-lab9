from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Books')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# books = [
#     {'author': 'Andy Weir',
#      'name': 'Project Hail Mary',
#      'id': 0},
#      {'author': 'Andy Weir',
#      'name': 'Martian',
#      'id': 0},
#      {'author': 'Yuval Noah Harari',
#      'name': 'Sapiens: A Brief History of Humankind',
#      'id': 0},
# ]

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def __repr__(self):
        return f'<Book{self.id} | {self.author} - {self.name}'

@app.route('/')
def main():
    books = Book.query.all()
    return render_template('index.html', book_list=books)

@app.route('/add', methods=['POST'])
def add_book():
    data = request.json
    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    return 'Ok'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

