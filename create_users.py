from main import User, Session, engine

new_user = User(id=100,username="Hasnain",email="hasnain@gmail.com")

session = Session(bind=engine)

session.add(new_user)
session.commit()
