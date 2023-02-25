from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import favorite, user, book

@app.route('/add/favorite', methods = ['POST'])
def add_fav():
    favorite.Favorite.save(request.form)

    return redirect(request.referrer)