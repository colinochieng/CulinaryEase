
from schema.recipe import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
import bcrypt
from datetime import datetime
from schema.address import Address
import uuid


PEPPER = b'culinarysuperpepper'

class User(Base):
    """User Class"""
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    username = Column(String(60), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password_hash = Column(String(60), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    profile_picture = Column(String(120), nullable=False, default='profile_picture.png')
    bios = Column(Text, nullable=True)
    recipes = relationship('Recipe', backref='artist')
    addresses = relationship('Address', backref='user')

    def __init__(self):
        self.id = str(uuid.uuid4())

    def set_passwd(self, password):
        """Hash the password"""
        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(PEPPER + password.encode('utf-8'), salt)
        self.password_hash = hashed_pwd.decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(PEPPER + password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def to_dict(self):
        """
        compose user object to a dictionary
        """
        data = self.__dict__

        data.pop('password_hash', None)

        if len(self.recipes) > 0:
            pass
        else:
            del data['recipes']
        if len(self.addresses) > 0:
            data.update({'addresses': data['addresses'][0].to_dict()})
        else:
            del data['addresses']

        data.pop('_sa_instance_state', None)
        data.pop('profile_picture', None)
        data.pop('created_at', None)
        data.pop('updated_at', None)

        return data
