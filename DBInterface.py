"""
Database Interface

Based on Sqlite3
"""
import sqlite3

class Database(object):
    """
    Handle connection with a database
    """

    def __init__(self, filename):
        """
        Create a connection with a database
        """
        
        self.filename = filename

        # Connect witht the database
        self.connection = sqlite3.connect(filename)

        # Get a cursor
        self.cursor = self.connection.cursor()

    def Execute(self, query, values=None):
        """
        Execute SQL query.
        Returns the result in an iterator
        """

        if values is None:
            return self.cursor.execute(query)
        else:
            return self.cursor.execute(query, values)

    def Commit(self):
        """
        Commit changes to the database
        """
        self.connection.commit()

    def Close(self):
        """
        Close connection with the database
        """
        self.connection.close()
