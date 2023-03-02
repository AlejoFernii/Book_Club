from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book, user
from flask import flash

class Favorite:
    DB = "book_club"
    def __init__(self,data):
        self.id = data['id']
        self.book_id = data['book_id']
        self.user_id = data['user_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO favorites (book_id, user_id) VALUES (%(book_id)s, %(user_id)s);"

        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def get_liked_by(cls,data):
        query = "SELECT * FROM favorites JOIN users ON favorites.user_id = users.id WHERE favorites.book_id = %(id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)

        liked_by = []
        print(results)
        for row in results:

            user_data = {
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'password':row['password'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at'],
            }

            one_user = user.User(user_data)

            liked_by.append(one_user)

        return liked_by
    

    @classmethod
    def get_all_favs_from_user(cls,data):
        query = "SELECT * FROM favorites JOIN books ON favorites.book_id = books.id WHERE favorites.user_id = %(id)s;"

        results = connectToMySQL(cls.DB).query_db(query,data)

        all_favs = []

        for row in results:

            book_data = {
                'id':row['books.id'],
                'user_id':row['user_id'],
                'title':row['title'],
                'description':row['description'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at'],
                'in_favs': False,
            }

            one_book = book.Book(book_data)

            all_favs.append(one_book)

        return all_favs
    


    @classmethod
    def destroy_favorite(cls,data):
        query = "DELETE FROM favorites WHERE book_id = %(book_id)s AND user_id = %(user_id)s;"

        return connectToMySQL(cls.DB).query_db(query,data)
