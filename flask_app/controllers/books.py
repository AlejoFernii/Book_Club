from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import favorite, user, book


@app.route('/create/book', methods=['POST'])
def create_book():
    valid_book = book.Book.validate_book(request.form)
    if valid_book:
        print('Book created successfully!')
        # newbook = book.Book.save(request.form)
        book.Book.save(request.form)
    return redirect('/home')

@app.route('/show/book/<int:id>')
def show_book(id):

    if 'user_id' not in session:
        return redirect('/')
    
    user_data = {'id':session['user_id']}
    current_user = user.User.get_one(user_data)

    data = {'id':id}

    one_book = book.Book.get_one(data)

    return render_template('show_book.html',current_user=current_user, one_book=one_book)

@app.route('/editPage/<int:id>')
def go_edit(id):

    if 'user_id' not in session:
        return redirect('/')

    user_data = {'id':session['user_id']}
    current_user = user.User.get_one(user_data)

    book_data = {'id':id}
    one_book = book.Book.get_one(book_data)

    return render_template('edit_book.html', current_user=current_user, one_book=one_book)

@app.route('/update/book', methods= ['POST'])
def edit_book():

    book.Book.update_book(request.form)

    return redirect('/home')


@app.route('/delete/book/<int:id>')
def delete_book(id):
    data = {'id':id}
    book.Book.destroy_book(data)

    return redirect('/home')
