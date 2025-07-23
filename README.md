#Crud.py

from sqlalchemy.orm import Session

from models import User

#insert new record into the database

def create_user(db: Session, name: str, email: str):

db_user User(name name, email=email)

db.add(db_user)

db.commit()

db.refresh(db_user)

return db user

#get all records from the database

def get_users(db: Session):

return db.query(User).all()

#update a user record in the database

def update_user(db: Session, user_id: int, name: str | None, email: str | None):

db_user= db.query(User).filter(User.id user_id).first()

if db_user:

if name is not None:

db_user.name = name

if email is not None:

db_user.email email

db.commit()

db.refresh(db_user)

return db_user

#delete a user record from the database

def delete_user(db: Session, user_id: int) -> bool:

db_user= db.query(User).filter(User.id == user_id).first()

if db_user:

db.delete(db_user)

db.commit()

return True

return False
