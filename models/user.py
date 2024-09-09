from common_import_modules import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False )
    email:Mapped[str] = mapped_column(unique=True, nullable=False)
    