from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['quote'], request.form['author'], request.form['date_of_quote'], request.form['source_type'], request.form['source_of_quote'],request.form['quote_rating'])
        return redirect(url_for('index'))
