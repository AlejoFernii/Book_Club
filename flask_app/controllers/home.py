from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, book, favorite

@app.route('/home')
def home():

    if 'user_id' not in session:
        return redirect('/')
    
    user_data = {'id':session['user_id']}
    current_user = user.User.get_one(user_data)

    all_favs = favorite.Favorite.get_all_favs_from_user(user_data)

    all_books = book.Book.get_all_with_user()

    return render_template('home.html', current_user=current_user, all_books=all_books, all_favs=all_favs)

@app.route('/create/book', methods=['POST'])
def create_book():
    valid_book = book.Book.validate_book(request.form)
    if valid_book:
        print('Book created successfully!')
        # newbook = book.Book.save(request.form)
        book.Book.save(request.form)
    return redirect('/home')