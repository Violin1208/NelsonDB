# coding: utf-8
# from sqlalchemy import Boolean, Column, Date, Integer, Text
# from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()
# metadata = Base.metadata


from nelsondb import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column, Date, Integer, Text
 
db = SQLAlchemy(app)

#sqlacodegen used: automatic model code generator
class Nelson(db.Model):
    __tablename__ = 'nelson'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    name = Column(Text)
    place = Column(Text)
    navy = Column(Boolean, nullable=False)
    navy_cat = Column(Text)
    family = Column(Boolean, nullable=False)
    friends = Column(Boolean, nullable=False)
    government = Column(Boolean, nullable=False)
    whig = Column(Boolean, nullable=False)
    tory = Column(Boolean, nullable=False)
    merchants = Column(Boolean, nullable=False)
    foreigners = Column(Boolean, nullable=False)
    foreigners_cat = Column(Text)
    usefulness = Column(Text)
    closeness = Column(Text)
    gov_cat = Column(Text)
    printed_primary_source = Column(Text)
    manuscript_source = Column(Text)


