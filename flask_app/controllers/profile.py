from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import favorite, user, book

@app.route('/profile/<int:id>')
def profile(id):

    if 'user_id' not in session:
        return redirect('/')

    user_data = {'id':session['user_id']}
    current_user = user.User.get_one(user_data)

    profile_data = {'id':id}
    profile_user = user.User.get_one(profile_data)

    all_books = book.Book.get_all_from_user(profile_data)

    all_favs = favorite.Favorite.get_all_favs_from_user(profile_data)

    return render_template('profile.html', current_user=current_user, profile_user=profile_user, all_books=all_books, all_favs=all_favs)

