from main import User, Session, engine


session= Session(bind=engine)

user = session.query(User).all()

print(user)