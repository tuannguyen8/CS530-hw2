class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, quote_id, quote, author, date_of_quote, source_type, source_of_quote, quote_rating):
        """
        Inserts entry into database
        :param name: String
        :param email: String
        :param message: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

    def delete (self,quote_id):
        """
        Delete an quote data in database
        :param quote_id: String
        :return: none
        :raises: Database errors on connection and deletion
        """
        pass

        # def select(sel, quote_id):
    #     """
    #     Gets all entries from the database
    #     :return: Tuple containing all rows of database
    #     """
    #     pass