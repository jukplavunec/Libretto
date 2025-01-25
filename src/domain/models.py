from datetime import datetime
from decimal import Decimal
from uuid import UUID

from src.domain.enums import BookState, UserState
from src.config import settings


class Book:
    def __init__(
        self, title: str, author: str, genre: str, year: int, book_id: UUID
    ) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.book_id = book_id
        self.state = BookState.AVAILABLE

    def set_state(self, new_state: BookState) -> None:
        self.state = new_state

    def __repr__(self) -> str:
        return f"Book(title={self.title}, author={self.author}, genre={self.genre}, year={self.year}, book_id={self.book_id}, state={self.state})"

    def __str__(self) -> str:
        return f"Book(title={self.title}, author={self.author}, genre={self.genre}, year={self.year}, book_id={self.book_id}, state={self.state})"


class User:
    def __init__(self, name: str, user_id: int, email: str) -> None:
        self.name = name
        self.user_id = user_id
        self.email = email
        self.user_state = UserState.COMMON
        self.issued_books: list[Book] = []

    def borrow_book(self, book: Book) -> None:
        if book.state == BookState.AVAILABLE:
            book.set_state(BookState.CHECKED_OUT)
            self.issued_books.append(book)
        else:
            raise ValueError("Book is not available")

    def return_book(self, book: Book) -> None:
        if book in self.issued_books:
            book.set_state(BookState.AVAILABLE)
            self.issued_books.remove(book)
        else:
            raise ValueError("Book is not issued to this user")

    def __repr__(self) -> str:
        return f"User(name={self.name}, user_id={self.user_id}, user_state={self.user_state}, issued_books={self.issued_books})"

    def __str__(self) -> str:
        return f"User(name={self.name}, user_id={self.user_id}, user_state={self.user_state}, issued_books={self.issued_books})"


class Loan:
    def __init__(self, book: Book, user: User, due_date: datetime) -> None:
        self.user = user
        self.book = book
        self.due_date = due_date
        self.returned_date: datetime | None = None

    def mark_returned(self) -> None:
        self.returned_date = datetime.now()

    def calculate_fine(self) -> Decimal:
        if self.returned_date and self.returned_date > self.due_date:
            overdue_days = (self.returned_date - self.due_date).days
            return self._calculate_fine_by_strategy(overdue_days, self.user)
        return Decimal(0.0)

    def _calculate_fine_by_strategy(self, overdue_days: int, user: User) -> Decimal:
        COEF_BY_STATUSES = {
            UserState.COMMON: settings.user_coefficients.common,
            UserState.VIP: settings.user_coefficients.vip,
            UserState.ADMIN: settings.user_coefficients.admin,
        }
        return Decimal(overdue_days * COEF_BY_STATUSES[user.user_state])
