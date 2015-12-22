import csv
import os
import sqlalchemy
from datetime import datetime

from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///matchdb.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Date

class Match(Base):
    __tablename__ = "matches"
    
    id = Column(Integer, primary_key=True)
    season = Column(String)
    div_ = Column(String)
    date_ = Column(Date)
    hometeam_ = Column(String)
    awayteam_ = Column(String)
    fthg_ = Column(Integer)
    ftag_ = Column(Integer)
    ftr_ = Column(String)
    hthg_ = Column(Integer)
    htag_ = Column(Integer)
    htr_ = Column(String)
    referee_ = Column(String)
    hs_ = Column(Integer)
    as_ = Column(Integer)
    hst_ = Column(Integer)
    ast_ = Column(Integer)
    hf_ = Column(Integer)
    af_ = Column(Integer)
    hc_ = Column(Integer)
    ac_ = Column(Integer)
    hy_ = Column(Integer)
    ay_ = Column(Integer)
    hr_ = Column(Integer)
    ar_ = Column(Integer)
    
    def __repr__(self):
        return "<Match(hometeam_='%s', awayteam_='%s')>" % (
            self.hometeam_, self.awayteam_)
            
Base.metadata.create_all(engine)
    
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()    

DATA_DIR = "data/"
REL_COLS = 23 #Number of Relevant columns

print os.getcwd()

for csv_file in os.listdir(os.getcwd() + "/" + DATA_DIR):
    print csv_file
    with open(DATA_DIR + csv_file, 'r') as f:
        reader = csv.reader(f)
        header = reader.next()
        header_keys = {h:{'index': idx, 'key': h.lower() + "_"} 
            for idx, h in enumerate(header[:REL_COLS])}
            
        if csv_file=="1213.csv":
            header_keys.pop("B365H")
        
        # print header[:REL_COLS]
        # print header_keys
        
        for row in reader:
            # print row
            match_data = {header_keys[h]['key']: row[header_keys[h]['index']] 
                for h in header_keys.keys()}
            match_data['date_'] = datetime.strptime(
                row[header_keys['Date']['index']], '%d/%m/%y')
            match_data['season'] = csv_file.strip(".csv")
            if csv_file=="1213.csv":
                match_data['referee_'] = ''
            # print match_data
            match = Match(**match_data)
            # print match
            session.add(match)
    # break

session.commit()



