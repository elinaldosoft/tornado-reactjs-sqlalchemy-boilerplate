from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import Column, Integer, String, TEXT, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import class_mapper

Base = declarative_base()


class ModelBase(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return "<%s(id='%s')>" % (self.__class__.__name__, getattr(self, 'id'))

    @property
    def serialize(self):
        columns = [c.key for c in class_mapper(self.__class__).columns]
        return dict((c, getattr(self, c)) for c in columns)


class Article(ModelBase):
    __tablename__ = "articles"
    title = Column(String(70))
    slug = Column(String(255))
    text = Column(TEXT)


class Comment(ModelBase):
    __tablename__ = "comments"
    name = Column(String(70))
    email = Column(String(255))
    text = Column(TEXT)
    article_id = Column(Integer, ForeignKey('articles.id'))
