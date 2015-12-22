from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///matchdb.db', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()  

rs=session.execute("select count(*) from matches")
print(rs.fetchone())