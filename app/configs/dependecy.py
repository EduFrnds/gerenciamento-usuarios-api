import sqlite3
from app.adapters.repositories import UserRepository
from app.domain.ports.user import UserPort

class UserRepositoryProvider:
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path

    def get_user_repository(self) -> UserPort:
        db_connection = sqlite3.connect(self.db_path, check_same_thread=False)
        return UserRepository(db_connection)