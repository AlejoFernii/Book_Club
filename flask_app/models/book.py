from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, favorite
from flask import flash, session


class Book:
    DB = "book_club"

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.creator = None
        self.liked_by = []
        self.in_favs = False

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (user_id, title, description) VALUES (%(user_id)s, %(title)s, %(description)s);"

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM books JOIN users ON books.user_id = users.id;"

        results = connectToMySQL(cls.DB).query_db(query)

        all_books = []

        fav_user_data = {'id':session['user_id']} 
        user_favs = favorite.Favorite.get_all_favs_from_user(fav_user_data)

        for row in results:

            one_book = cls(row)

            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            one_user = user.User(user_data)

            for b in user_favs:
                if one_book.id == b.id:
                    one_book.in_favs = True

            one_book.creator = one_user
            fav_data = {'id': one_book.id}
            favorites = favorite.Favorite.get_liked_by(fav_data)
            for fav in favorites:

                one_book.liked_by.append(fav)

            all_books.append(one_book)

        return all_books

    @classmethod
    def get_all_from_user(cls,data):
        query = "SELECT * FROM books JOIN users ON books.user_id = users.id WHERE users.id = %(id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)

        all_books = []

        fav_user_data = {'id':session['user_id']} 
        user_favs = favorite.Favorite.get_all_favs_from_user(fav_user_data)

        for row in results:

            one_book = cls(row)

            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            for b in user_favs:
                if one_book.id == b.id:
                    one_book.in_favs = True

            one_user = user.User(user_data)

            one_book.creator = one_user

            all_books.append(one_book)

        return all_books

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books JOIN users ON books.user_id = users.id WHERE books.id = %(id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)
        fav_user_data = {'id':session['user_id']} 
        user_favs = favorite.Favorite.get_all_favs_from_user(fav_user_data)
        for row in results:

            one_book = cls(row)

            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }

            for b in user_favs:
                if one_book.id == b.id:
                    one_book.in_favs = True

            one_user = user.User(user_data)

            one_book.creator = one_user

            fav_data = {'id':row['id']}
            all_favs = favorite.Favorite.get_liked_by(fav_data)
            for fav in all_favs:
                one_book.liked_by.append(fav)

        date = {'id':row['id']}
        posted = cls.date_posted(date)

        one_book.created_at = posted

        return one_book
    
    @classmethod
    def date_posted(cls,data):
        query = "SELECT DATE_FORMAT(created_at, '%%%%M %%%%D %%%%Y') AS date FROM books WHERE id = %(id)s;"

        result = connectToMySQL(cls.DB).query_db(query,data)

        return result[0]['date']

    @classmethod
    def update_book(cls, data):
        query = "UPDATE books SET title = %(title)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def destroy_book(cls, data):
        query = "DELETE FROM books WHERE id = %(id)s;"

        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_book(book):
        is_valid = True
        if len(book['title']) < 2:
            flash("Title Min. 10 Characters.", 'book')
            is_valid = False
        if len(book['description']) < 10:
            flash("Description Must Be At least 10 Characters Long.", 'book')
            is_valid = False
        return is_valid
