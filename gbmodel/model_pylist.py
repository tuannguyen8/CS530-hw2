"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.guestentries = []

    def select(self):
        """
        Returns guestentries list of lists
        Each list in guestentries contains: quote_id, quote, quote, author, date_of_quote, source_type, source_of_quote, quote_rating
        :return: List of lists
        """
        return self.guestentries

    def insert(self, quote_id, quote, author, date_of_quote, source_type, source_of_quote, quote_rating):
        """
        Appends a new list of values representing new message into guestentries
        :param quote_id: String
        :param quote: String
        :param author: String
        :param date_of_quote: String
        :param source_type: String
        :param source_of_quote: String
        :param quote_rating: Integer
        :return: True
        """
        params = [quote_id, quote, author, date_of_quote, source_type, source_of_quote, quote_rating]
        self.guestentries.append(params)
        return True
    
    def delete(self, quote_id):
        """
        Deletes an entry from guestentries based on quote_id
        :param quote_id: String
        :return: True if the entry was found and deleted, False otherwise
        """
        for entry in self.guestentries:
            if entry.quote_id == quote_id:
                self.guestentries.remove(entry)
                return True
        return False
    
    # def get_by_id(self, quote_id):
    #     """
    #     Returns guestentries list of lists
    #     Each list in guestentries contains: name, email, date, message
    #     :return: List of lists
    #     """
    #     for entry in self.guestentries:
    #         if entry.quote_id == quote_id:
    #             return entry
    #     return False
    #Tuan update
    # def update(self, quote_id):
    #     """
    #     Deletes an entry from guestentries based on quote_id
    #     :param quote_id: String
    #     :return: True if the entry was found and deleted, False otherwise
    #     """
    #     for entry in self.guestentries:
    #         if entry[0].quote_id == quote_id:
    #             self.guestentries.remove(entry)
    #             return True
    #     return False
