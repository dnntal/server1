from flask import Flask,jsonify

app = Flask(__name__)



books = [
    {'id': 0,
     'title': 'Harry Potter1',
     'author': 'j.K',
     'year_published': '2001'},
    {'id': 1,
     'title': 'Harry Potter2',
     'author': 'j.K ',
     'published': '2002'},
    {'id': 2,
     'title': 'Harry Potter3',
     'author': 'J.K. ',
     'published': '2003'}
]



@app.route('/', methods=['GET'])
def index():
    return "<h1>books</h1><p>Hello world</p>"

@app.route('/book/all', methods=['GET'])
def api_all():
    return jsonify(books)




app.run(debug = True )
