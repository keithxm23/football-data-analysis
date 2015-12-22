from prettytable import PrettyTable
from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///matchdb.db', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()  

def runsql(sql):
    rs=session.execute(sql)
    col_names = [cn for cn in rs.keys()]
    results = rs.fetchall()
    x = PrettyTable(col_names)
    x.align="l" #left align values in rows
    for r in results:
        x.add_row(r)
    #     # print r
    print(x)
        
        
runsql("select count(*) from matches")