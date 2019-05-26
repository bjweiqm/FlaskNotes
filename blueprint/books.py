from flask import Blueprint

book_bp = Blueprint('book', __name__)


@book_bp.route('/books_list/')
def books_list():

    return 'Books list'

