from sqlalchemy import Column, Integer, String

from database import Base

class User (Base):

_tablename = "users"

id = Column(Integer, primary_key=True, index=True)

name Column (String (50), index=True, nullable=False)

email = Column (String (100), unique=True, index=True, nullable=False)

def _repe_(self):

return f"<User(id={self.id), name={self.name}, email={self.email})>"
