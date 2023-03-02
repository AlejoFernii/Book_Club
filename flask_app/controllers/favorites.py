from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import favorite, user, book

@app.route('/add/favorite', methods = ['POST'])
def add_fav():
    favorite.Favorite.save(request.form)

    return redirect(request.referrer)

@app.route('/delete/favorite/<int:book_id>/<int:user_id>')
def delete_fav(book_id,user_id):

    current_user = session['user_id']

    data = {
        'book_id': book_id,
        'user_id': user_id,
    }

    favorite.Favorite.destroy_favorite(data)

    return redirect(f'/profile/{current_user}')