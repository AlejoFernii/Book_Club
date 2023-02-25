from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, favorite
from flask import flash


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

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (user_id, title, description) VALUES (%(user_id)s, %(title)s, %(description)s);"

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM books JOIN users ON books.user_id = users.id;"

        results = connectToMySQL(cls.DB).query_db(query)

        all_books = []

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

            fav_data = {'id': one_book.id}
            favorites = favorite.Favorite.get_liked_by(fav_data)
            print(favorites)
            for fav in favorites:
                # like_by_data = {
                #     'id': fav['users.id'],
                #     'first_name': fav['first_name'],
                #     'last_name': fav['last_name'],
                #     'email': fav['email'],
                #     'password': fav['password'],
                #     'created_at': fav['created_at'],
                #     'updated_at': fav['updated_at'],
                # }
                # one_favorite = user.User(like_by_data)

                one_book.liked_by.append(fav)

            one_user = user.User(user_data)

            one_book.creator = one_user

            all_books.append(one_book)

        return all_books

    @classmethod
    def get_all_from_user(cls):
        query = "SELECT * FROM books JOIN users ON book.user_id = users.id WHERE users.id = %(id)s;"

        results = connectToMySQL(cls.DB).query_db(query)

        all_books = []

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

            one_book.creator = one_user

            all_books.append(one_book)

        return all_books

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books JOIN users ON books.user_id = users.id WHERE users.id = %(id)s;"

        results = connectToMySQL(cls.DB).query_db(query)

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

            one_book.creator = one_user

        return one_book

    @classmethod
    def update_book(cls, data):
        query = "UPDATE books SET title = %(title)s, description = %(description), updated_at = NOW() WHERE id = %(id)s;"

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
