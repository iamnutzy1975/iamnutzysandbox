import datetime
import pandas as pd
from dateutil.rrule import rrule, DAILY
from operator import itemgetter
import numpy as np

FILE = 'file2.csv'

#read in the file, but only columns specified (header row)
#header row is omited.
df = pd.read_csv(FILE, usecols=['date', 'trend'])
#transform the datafram to the list of tuples
scores = list(df.itertuples(index=False, name=None))
#caculate the difference between the first and last date, assumed import data is already sorted
minDate = datetime.datetime.strptime(scores[0][0], '%Y-%m-%d').date()
maxDate = datetime.datetime.strptime(scores[-1][0], '%Y-%m-%d').date()
delta = (maxDate-minDate).days

#Create a new list named trendline filled with zeros and the length of diff_days
trendline = [0] * delta

index = 0
for k,dt in enumerate(rrule(DAILY, dtstart=minDate, until=maxDate)):
    if dt.strftime("%Y-%m-%d") == scores[index][0]:
        #date exists in scores
        trendline[k] = scores[index][1]
        index += 1

decay = np.exp(-1 / 100.0) #np is numpy, can be calculated also with standard python math lib
for i, t in enumerate(trendline):
    if trendline[i] != 0 or i == 0: continue #if we have value then don't change it
    trendline[i] = decay * trendline[i-1] #this is a gap, take previous value and add a 1 day decay to it

print maxDate
print minDate
print delta
print trendline