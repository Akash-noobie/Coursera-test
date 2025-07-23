from database import SessionLocal, engine, Base

from crud import (

create_user,

get_users,

update_user,

delete_user

)

def init_db():

# Create the database tables

Base.metadata.create_all (bind=engine)

2

B

def demo_crud():

コ

db = SessionLocal()

print("Creating users...")

user1 = create_user(db, name="Alice", email="a@mail.com")

print(f"Created: {user1}")
