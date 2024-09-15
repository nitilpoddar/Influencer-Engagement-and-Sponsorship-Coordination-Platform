from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Define Base class
class Base(DeclarativeBase):
    pass

# Define db instance
db = SQLAlchemy(model_class=Base)
