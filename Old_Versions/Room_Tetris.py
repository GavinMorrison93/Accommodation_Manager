import numpy as np
import pandas as pd
import datetime

from datetime import datetime
from datetime import date
# from datetime import time

from datetime import time, tzinfo, timedelta

import time

now = datetime.now()

time_data = now.strftime("%H.%M.%S")

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

date_data = now.strftime("%d-%m-%Y")

# t = time(format)

# time = datetime 
# t = datetime.time(datetime.now())

data = pd.read_csv("Test_Data.csv")

print("\nEntire Table: \n", data)

dh = data.head()
print("\nFirst Five Entries: \n", dh)

pa = data['Previous Attendance'].mean()
print("\nPrevious Attendance Average: \n", pa)

toploc = data['Location'].value_counts().head(1)
print("\nLocation with most applicants :\n", toploc)

filename = "C:/Users/Gav/Desktop/Accommodation_Manager/test/export_dataframe_" + date_data + "_" + time_data + ".csv"

# filename = "export_dataframe_" + str(date.today()) + "_" + t + ".csv"

# filename = "export_dataframe_" + str(date.today()) + "_" + str(datetime.time(datetime.now())) + ".csv"

# filename = "export_dataframe_" + str(datetime.now()) + "_" + str(t.strftime("%H:%M:%S")) + ".csv"

# filename = "export_dataframe_" + str(date.today()) + "_" + str(time.isoformat()) + ".csv"

# filename = "export_dataframe_" + str(datetime.now()) + ".csv"

# export_csv = toploc.to_csv (r'C:\Users\Gav\Desktop\Accommodation_Manager\export_dataframe.csv', index = None, header=True)

export_csv = toploc.to_csv (filename, index = None, header=True)

# export_csv = toploc.to_csv (r' (str(date.today()))', index = None, header=True)

# "file-" + str(date.today()) + ".txt"