


class User(db.Model):
    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False )
    email:Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    u_type: Mapped[str] = mapped_column(nullable=False)

