"""
A simple quotation flask app.
Data is stored in a SQLite database that looks something like the following:

+---------------------------------------+-------------------------------------+----------------------+---------------+-------------|----------------------------------|--------------+
| quote_id                              | quote                               | author               | date_of_quote | source_type | source_of_quote                  | quote_rating |
+=======================================+=====================================+======================+===============+=============+==================================+==============|
| 15e9687c-e64b-4be3-976f-f8bcb2c39325  |  Well done is better than well said | Benjamin Franklin    | 4/26/2024     | Speak       | Stanford University Commencement | 5            |
+---------------------------------------+-------------------------------------+----------------------+---------------+-------------+----------------------------------+--------------+

This can be created with the following SQL (see bottom of this file):

    create table quotation (quote_id text, quote text, author text, date_of_quote date, source_type text, source_of_quote text, quote_rating number)

"""
from datetime import date
from .Model import Model
import sqlite3
import uuid
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from quotation")
        except sqlite3.OperationalError:
            #cursor.execute("create table quotation (quote_id text, quote text, author text, date_of_quote date, source_type text, source_of_quote text, quote_rating number)")
            cursor.execute("create table if not exist quotation (quote_id text, quote text, author text, date_of_quote date, source_type text, source_of_quote text, quote_rating number)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM quotation")
        return cursor.fetchall()
    

    def insert(self, quote, author, date_of_quote, source_type, source_of_quote, quote_rating ):
        """
        Inserts entry into database
        :param quote_id: String
        :param quote: String
        :param author: String
        :param date_of_quote: Date
        :param source_type: String
        :param source_of_quote: String
        :param quote_rating: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'quote_id': str(uuid.uuid4()), 'quote':quote, 'author':author, 'date_of_quote':date_of_quote, 'source_type':source_type,
                   'source_of_quote':source_of_quote, 'quote_rating': quote_rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into quotation (quote_id, quote, author, date_of_quote, source_type, source_of_quote, quote_rating) VALUES (:quote_id, :quote, :author, :date_of_quote, :source_type, :source_of_quote, :quote_rating)", params)
        
        connection.commit()
        cursor.close()
        return True
    
    def delete(self, quote_id):
        """
        Detele quotation from database
        :param quote_id: String
        :param quote: String
        :param author: String
        :param date_of_quote: Date
        :param source_type: String
        :param source_of_quote: String
        :param quote_rating: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        try:
            params = {'quote_id': quote_id}
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()
            cursor.execute("delete from quotation where quote_id = :quote_id", {'quote_id':quote_id})

            connection.commit()
            cursor.close()
            return True
        except sqlite3.Error as e:
            # Handle database errors
            print("Error deleting entry:", e)
            return False
        
    # def update(self, quote_id, quote, author, date_of_quote, source_type, source_of_quote, quote_rating):
    #     """
    #     Update an existing quote in the database.
        
    #     Parameters:
    #         quote_id (int): The ID of the quote to be updated.
    #         quote (str): The updated quote text.
    #         author (str): The updated author of the quote.
    #         date_of_quote (str): The updated date when the quote was made.
    #         source_type (str): The updated type of the source of the quote.
    #         source_of_quote (str): The updated source of the quote.
    #         quote_rating (int): The updated rating of the quote.
        
    #     Returns:
    #         bool: True if the update is successful, False otherwise.
    #     """
    #     try:
    #         params = {
    #             'quote_id': quote_id,
    #             'quote': quote,
    #             'author': author,
    #             'date_of_quote': date_of_quote,
    #             'source_type': source_type,
    #             'source_of_quote': source_of_quote,
    #             'quote_rating': quote_rating
    #         }
    #         connection = sqlite3.connect(DB_FILE)
    #         cursor = connection.cursor()
    #         cursor.execute("""
    #             UPDATE quotation 
    #             SET quote = :quote, author = :author, date_of_quote = :date_of_quote,
    #             source_type = :source_type, source_of_quote = :source_of_quote,
    #             quote_rating = :quote_rating
    #             WHERE quote_id = :quote_id
    #             """, params)

    #         connection.commit()
    #         cursor.close()
    #         return True
    #     except sqlite3.Error as e:
    #         # Handle database errors
    #         print("Error updating entry:", e)
    #         return False
        
    # def get_by_id(self, quote_id):
    #     """
    #     Gets a row from the database by its quote_id
    #     :param quote_id: The quote_id of the row to retrieve
    #     :return: The row as a tuple if found, otherwise None
    #     """
    #     try:
    #         connection = sqlite3.connect(self.DB_FILE)
    #         cursor = connection.cursor()
    #         cursor.execute("SELECT * FROM quotation WHERE quote_id = ?", (quote_id,))
    #         return cursor.fetchone()
    #     except sqlite3.Error as e:
    #         print("Error fetching item:", e)
    #         return None


