from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import 
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    DB = 'book_club'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['password']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
        self.favorites = []

    @classmethod
    def create(cls, data):
        query = """ INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(),NOW()); """

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"

        result = connectToMySQL(cls.DB).query_db(query, data)

        return cls(result[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        return connectToMySQL(cls.DB).query_db(query)

    # @classmethod
    # def get_by_username(cls,data):
    #     query = "SELECT * FROM users WHERE username = %(username)s;"
    #     result = connectToMySQL('wall').query_db(query,data)
    #     if len(result) < 1:
    #         return False
    #     return cls(result[0])


    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    


    @staticmethod
    def validate(member):
        is_valid = True
        if len(member['first_name']) <= 2:
            flash("First Name Required.", 'reg')
            is_valid = False
        if len(member['last_name']) <= 2:
            flash("Last Name Required.", 'reg')
            is_valid = False
        if len(member['pw']) < 8:
            flash("Password Must Be At Least 8 Characters.", 'reg')
            is_valid = False
        if not EMAIL_REGEX.match(member['email']):
            flash("Invalid Email Format.", 'reg')
            is_valid = False
        if member['confirm'] != member['password']:
            flash("Password Must Match.", 'reg')
            is_valid = False
        return is_valid
