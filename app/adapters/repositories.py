from app.domain.models.user import User
from app.domain.ports.user import UserPort

class UserRepository(UserPort):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    async def get_all_users(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        return [User.model_validate(dict(id=row[0], user_name=row[1], user_email=row[2])) for row in rows]

    async def get_user_by_id(self, user_id: int) -> User | None:
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            return User.model_validate(dict(id=row[0], user_name=row[1], user_email=row[2]))
        return None

    async def create_user(self, user: User) -> User:
        cursor = self.db_connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.user_name, user.user_email)
        )
        self.db_connection.commit()
        user.id = cursor.lastrowid  # Set the new user's ID
        return user

    async def update_user(self, user: User) -> User | None:
        cursor = self.db_connection.cursor()
        cursor.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (user.user_name, user.user_email, user.id)
        )
        self.db_connection.commit()
        if cursor.rowcount > 0:
            return user
        return None

    async def delete_user(self, user_id: int):
        cursor = self.db_connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.db_connection.commit()