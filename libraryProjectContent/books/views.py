from flask import Blueprint, url_for, redirect, render_template, flash, session
from libraryProjectContent.books.forms import AddBook
from libraryProjectContent.models import Book
from libraryProjectContent import db

book = Blueprint('books',__name__,
                  template_folder='templates/books')


@book.route('/addBook', methods=["GET","POST"])
def add():

    addform = AddBook()

    if addform.validate_on_submit():
        
        book = Book(id = addform.id.data,
                    ISBN = addform.ISBN.data,
                    title = addform.title.data,
                    author = addform.author.data,
                    publisher = addform.publisher.data,
                    description = addform.description.data)

        db.session.add(book)
        db.session.commit()

        flash(f"The book has been added successfully!")

        return redirect(url_for('books.add'))
    
    return render_template('managebooks.html',  addform=addform)
