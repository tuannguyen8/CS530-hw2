from flask import redirect, request, url_for, render_template, jsonify
from flask.views import MethodView
import gbmodel

class Update(MethodView):
    def get_by_id(self, quote_id):
        quote_id = quote_id

        model = gbmodel.get_model()
        entry = model.get_by_id(quote_id)
        entry = [dict(quote_id=row[0],quote=row[1], author=row[2], date_of_quote=row[3], source_type=row[4], source_of_quote=row[5], quote_rating=row[6]) for row in model.select()]
        
        if entry:
            return render_template('update.html',entry=entry)
        else:
            return jsonify({'error': 'Entry not found'}), 404

    # def post(self,quote_id):
    #     """
    #     Accepts POST requests, and processes the form;
    #     Redirect to index when completed.
    #     """
    #     model = gbmodel.get_model()
    #     # model.insert(request.form['name'], request.form['email'], request.form['message'], request.form['quote'])
    #     model.insert(request.form['quote'], request.form['author'], request.form['date_of_quote'], request.form['source_type'], request.form['source_of_quote'],request.form['quote_rating'])
    #     return redirect(url_for('index'))