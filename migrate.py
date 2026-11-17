from sqlalchemy import text
from database import engine
import models

models.Base.metadata.create_all(bind=engine)
with engine.begin() as connection:
    columns = [
        row[1]
        for row in connection.execute(text("PRAGMA table_info(tasks)"))
    ]
    if "user_id" not in columns:
        connection.execute(
            text("ALTER TABLE tasks ADD COLUMN user_id INTEGER REFERENCES users(id)")
        )

    if "priority" not in columns:
        connection.execute(
            text("ALTER TABLE tasks ADD COLUMN priority VARCHAR DEFAULT 'Medium'")
        )

    if "status" not in columns:
        connection.execute(
            text("ALTER TABLE tasks ADD COLUMN status VARCHAR DEFAULT 'Pending'")
        )

print("Database updated successfully!")