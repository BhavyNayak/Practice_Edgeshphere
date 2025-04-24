# 81. Write a program to read CSV data into a list of dictionaries.
import csv

with open('tgt.csv',newline='') as f :
    list(csv.DictReader(f))