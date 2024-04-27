"""
A simple guestbook flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from sign import Sign
from update import Update

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/delete/<quote_id>',
                 view_func=Index.as_view('delete_entry'),
                 methods=['POST'])

app.add_url_rule('/update/<quote_id>',
                 view_func=Update.as_view('update'),
                 methods=['GET'])

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET'])

app.add_url_rule('/sign',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
