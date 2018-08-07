from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password = Column(String(64))
    email = Column(String(250))
    name = Column(String(250), nullable=False)
    picture = Column(String(250))

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class Manufacturer(Base):
    __tablename__ = 'manufacturer'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    corporate_city = Column(String(250))
    created_date = Column(String(50))
    picture = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'corporate_city': self.corporate_city,
            'created_date': self.created_date
            
        }

class Software(Base):
    __tablename__ = 'software'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(String(10))
    year_published = Column(Integer)
    category = Column(String(100))
    created_date = Column(String(50))
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    manufacturer = relationship(Manufacturer)
    user_id = Column(Integer, ForeignKey('user.id'))
    

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'year_published': self.year_published,
            'category': self.category,
            'created_date': self.created_date
            
            
        }

engine = create_engine('sqlite:///softwarecatalog.db')


Base.metadata.create_all(engine)