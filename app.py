from flask import Flask, render_template

app = Flask('Task :3')

books = [
    {'author': 'Andy Weir',
     'name': 'Project Hail Mary'},
     {'author': 'Andy Weir',
     'name': 'Martian'},
     {'author': 'Yuval Noah Harari',
     'name': 'Sapiens: A Brief History of Humankind'},
]


@app.route('/')
def main():
    return render_template('index.html', 
                           book_list=books)


if __name__ == '__main__':
    app.run(debug=True)
