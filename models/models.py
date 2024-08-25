from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class Users(db.Model):
    

