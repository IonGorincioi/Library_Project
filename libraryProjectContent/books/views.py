from flask import Blueprint, url_for, redirect, render_template, flash, session
from libraryProjectContent.books.forms import AddBook
from libraryProjectContent.models import Book
from libraryProjectContent import db

book = Blueprint('books',__name__,
                  template_folder='templates/books')


@book.route('/addBook', methods=["GET","POST"])
def add():
    book = None
    addform = AddBook()

    if addform.validate_on_submit():
        book = Book.query.filter_by(id = addform.ISBN.data).first()
        if book is None:

            book = Book(id = addform.id.data,
                        ISBN = addform.ISBN.data,
                        title = addform.title.data,
                        author = addform.author.data,
                        publisher = addform.publisher.data,
                        description = addform.description.data)
            
            #  Add and save data into database
            db.session.add(book)
            db.session.commit()
        
        book = addform.book.data

        #  clear the form
        addform.ISBN.data=''
        addform.title.data=''
        addform.author.data=''
        addform.publisher.data=''
        addform.description.data=''
 

        flash(f"The book has been added successfully!")
        return redirect(url_for('books.add'))
    
    new_books = Book.query.order_by(Book.id)
    return render_template('managebooks.html',  addform=addform, 
                                                book=book,
                                                new_books=new_books)
