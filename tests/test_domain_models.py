import pytest
from faker import Faker

from uuid import uuid4
from src.domain.enums import BookState
from src.domain.models import Book, Loan, User

faker = Faker()

def test_book_change_state():
    book = Book(
        title=faker.pystr(),
        author=faker.pystr(),
        genre=faker.pystr(),
        year=faker.pyint(),
        book_id=uuid4(),
    )
    assert book.state == BookState.AVAILABLE
    book.set_state(BookState.CHECKED_OUT)
    assert book.state == BookState.CHECKED_OUT


def test_user_borrow_book():
    user = User(name=faker.pystr(), user_id=uuid4(), email=faker.email())
    book = Book(
        title=faker.pystr(),
        author=faker.pystr(),
        genre=faker.pystr(),
        year=faker.pyint(),
        book_id=uuid4(),
    )
    assert book.state == BookState.AVAILABLE
    user.borrow_book(book)
    assert book.state == BookState.CHECKED_OUT
    assert user.issued_books == [book]


def test_user_return_book():
    user = User(name=faker.pystr(), user_id=uuid4(), email=faker.email())
    book = Book(
        title=faker.pystr(),
        author=faker.pystr(),
        genre=faker.pystr(),
        year=faker.pyint(),
        book_id=uuid4(),
    )
    user.borrow_book(book)
    assert book.state == BookState.CHECKED_OUT
    assert user.issued_books == [book]
    user.return_book(book)
    assert book.state == BookState.AVAILABLE
    assert user.issued_books == []


def test_loan_mark_returned():
    user = User(name=faker.pystr(), user_id=uuid4(), email=faker.email())
    book = Book(
        title=faker.pystr(),
        author=faker.pystr(),
        genre=faker.pystr(),
        year=faker.pyint(),
        book_id=uuid4(),
    )
    user.borrow_book(book)
    loan = Loan(book, user, faker.date_time_this_year())
    loan.mark_returned()
    assert loan.returned_date


def test_loan_calculate_fine():
    user = User(name=faker.pystr(), user_id=uuid4(), email=faker.email())
    book = Book(
        title=faker.pystr(),
        author=faker.pystr(),
        genre=faker.pystr(),
        year=faker.pyint(),
        book_id=uuid4(),
    )
    user.borrow_book(book)
    loan = Loan(book, user, faker.date_time_this_year())
    loan.mark_returned()
    assert loan.calculate_fine()
