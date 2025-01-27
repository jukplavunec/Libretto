# 📚 Libretto

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-008080?style=for-the-badge&logo=python&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-4682B4?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-FFD43B?style=for-the-badge&logo=python&logoColor=darkblue)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Dynaconf](https://img.shields.io/badge/Dynaconf-F28D00?style=for-the-badge&logo=python&logoColor=white)
![Structlog](https://img.shields.io/badge/Structlog-5C2D91?style=for-the-badge&logo=python&logoColor=white)

Welcome to the **Libretto**! This is a platform where users can rent books online for a symbolic fee. Built with modern Python technologies, it offers a robust, scalable, and user-friendly experience.

---

## 🚀 Features

- Rent books online with ease.
- Manage book inventory and user rentals.
- Reliable and scalable backend powered by FastAPI.
- Database migrations and schema management with Alembic.
- Strong data validation using Pydantic.
- Configurable settings with Dynaconf.
- Structured logging with Structlog.
- Comprehensive testing suite with Pytest.

---

## 🛠️ Technologies Used

- **FastAPI**: For building the high-performance API.
- **SQLAlchemy**: ORM for database interactions.
- **Alembic**: Database migration tool.
- **Pydantic**: For data validation and settings management.
- **Pytest**: Testing framework.
- **Dynaconf**: Simplified configuration management.
- **Structlog**: For structured logging and better debugging.

---

## 🏗️ Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/book-rental-service.git
   cd book-rental-service
   ```

2. **Create a Virtual Environment:**
   ```bash
   poetry env use python3.13
   ```

3. **Install Dependencies:**
   ```bash
   poetry install
   ```

4. **Run Database Migrations:**
   ```bash
   make upgrade
   ```

5. **Start the Application:**
   ```bash
   make run
   ```

---

## ✅ Running Tests

Run the test suite with Pytest:

```bash
make test
```

---

## 📖 Documentation

Once the application is running, you can access the interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/api/v1/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/api/v1/redoc)
