import flask
from property import Property
app = flask.Flask(__name__)

property = Property(1, 'Land', 40000, "123 simple street", 2, 2, 20000, 40000)
@app.route('/')
def index():
    return f'{property}'