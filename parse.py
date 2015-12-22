import csv
import os

DATA_DIR = "data/"

print os.getcwd()

for csv_file in os.listdir(os.getcwd() + "/" + DATA_DIR):
    print csv_file
    with open(DATA_DIR + csv_file, 'r') as f:
        reader = csv.reader(f)
        header = reader.next()
        print header[:23]
        #for row in reader:
            #print row

