


class Influencer(db.Model):
    user_id: Mapped[int] = mapped_column(foreignKey('User.user_id'))
    followers: Mapped[str] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable = False)
