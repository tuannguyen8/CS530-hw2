from flask import render_template, request, jsonify
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(quote_id=row[0],quote=row[1], author=row[2], date_of_quote=row[3], source_type=row[4], source_of_quote=row[5], quote_rating=row[6]) for row in model.select()]
        return render_template('index.html',entries=entries)

    def post(self, quote_id):
        # Get the quote_id from the URL parameters
        quote_id = quote_id

        # Delete the quotation with the given quote_id from the database
        model = gbmodel.get_model()
        deleted_entry = model.delete(quote_id)

        if deleted_entry:
            return jsonify({'message': 'Entry deleted successfully'})
        else:
            return jsonify({'error': 'Entry not found'}), 404