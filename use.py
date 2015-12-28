from prettytable import PrettyTable
from sqlalchemy import create_engine

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' #Regular color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///matchdb.db', echo=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()  

def runsql(sql, colorize=None):
    rs=session.execute(sql)
    col_names = [cn for cn in rs.keys()]
    results = rs.fetchall()
    x = PrettyTable(col_names)
    x.align="l" #left align values in rows

    ftr_color_map = {
            'H': bcolors.OKGREEN, 
            'A' : bcolors.FAIL,
            'D': bcolors.WARNING
            }

    for r in results:
        row = list(r)
        if colorize is not None:
            for c in colorize:
                try:
                    column_name = c['column']
                    color_map = c['color_map']
                    column_color = color_map[row[col_names.index(column_name)]]
                    row[col_names.index(column_name)] = column_color + row[col_names.index(column_name)] + bcolors.ENDC 
                except ValueError:
                    pass
        x.add_row(row)
    #     # print r
    print(x)


FTR_COLOR_MAP ={
        'H': bcolors.OKGREEN + bcolors.BOLD, 
        'A' : bcolors.FAIL + bcolors.BOLD,
        'D': bcolors.WARNING + bcolors.BOLD
        }


runsql("select count(*) from matches")
runsql("select hometeam_, awayteam_, ftr_ from matches where hometeam_='Arsenal' limit 10", 
        colorize=[
            {'column':'ftr_', 
            'color_map':FTR_COLOR_MAP
            }
        ])

print '...'
