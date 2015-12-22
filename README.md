

#scraper.py
Scrapes football-data.co.uk and downloads csv files for Premier League 

#parser.py


#Data fixes
Removed non-unicode, 8bit bytestrings  used as a leading space-character 
in Referee names from 0405.csv since it caused issues with parsing the data
Lines: 337 - 345

Referee data fixes:
| 0910   | 2009-11-07 | Wolves    | Arsenal   | St Bennett  => "S Bennett"
| 0910   | 2009-11-08 | Chelsea   | Man United | Mn Atkinson => "M Atkinson"
| 0910   | 2009-11-28 | Wigan     | Sunderland | Mn Atkinson => "M Atkinson"
| 0607   | 2007-04-06 | Everton   | Fulham    | D Gallagh => "D Gallagher"
| 0607   | 2007-05-05 | Reading   | Watford   | D Gallaghe => "D Gallagher"
| 0304   | 2003-08-23 | Southampton | Birmingham | Graham Barber => "G Barber"
| 0304   | 2003-09-20 | Newcastle   | Bolton     | Graham Barber => "G Barber"
