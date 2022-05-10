from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Provider(Base):
    __tablename__ = 'provider'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    sex = Column(String)
    birth_date = Column(Date)
    rating = Column(String)
    primary_skills = Column(String)
    secondary_skill= Column(String)
    company = Column(String)
    active = Column(Boolean)
    country = Column(String)
    language = Column(String)

    def __repr__(self):
        return "<Provider(first_name='{}', last_name='{}')>".format(self.first_name, self.last_name)