from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://janie:yolo@localhost/dynamicboard')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

class Email(Base):
  __tablename__ = 'boardcolors'

  id = Column(Integer)
  color = Column(Text)

  def __init__(self, id=None, color=None):
  	self.id = id
  	self.color = color

  def to_json(self):
  	return {'id': self.id, 'color': self.color}

def init_db():
  # creates all tables in engine
  Base.metadata.create_all(bind=engine)