from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask('Books')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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


@app.route('/delete/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return 'Ok'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

