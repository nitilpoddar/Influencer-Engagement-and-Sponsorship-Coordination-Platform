# All the models will have this commonality of import

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

#creating a base class for creating a db object using the SQLAlchemy constructor
# we are creating a seperate base class because if we want to add any custom functionality to our class then all the models would be able to inherit it

class Base(DeclarativeBase): #here DeclarativeBase is a subclass
    pass

db = SQLAlchemy(Base) # this is the db object I hhave created using the SQLAlchemy constructor

