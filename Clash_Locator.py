#--------------------------------------
# Code written by Gavin Morrison - 2020
#--------------------------------------
import numpy as np
import pandas as pd
from datetime import datetime
import csv
import os

#Date and time for exported files
now = datetime.now()
time_data = now.strftime("%H.%M.%S")
date_data = now.strftime("%d-%m-%Y")

#Imported original CSV data.
clash_data = pd.read_csv("Test_Data/Clash_Test.csv")
clash_data2 = pd.read_csv("Test_Data/Clash_Test.csv")

shared_rooms = clash_data[clash_data["Type of Room"]=="Shared"]

#Comparison for sorting loop 
clash_search = sorted(set(clash_data['Name']).intersection(set(clash_data2['Share with'])))

#Variable for export with duplicates
exported_file = "C:/Users/Gav/Desktop/Accommodation_Manager/Temp/clashes.csv"

#Create CSV file for export with header line only
f = open(exported_file, "w", newline='')
writer = csv.DictWriter(
    f, fieldnames=[" ", "Name", "Type of Room", "Share with", "Not Share With"])
writer.writeheader()
f.close()

#Sort Shared Room applicants    
for i in clash_search: 
         
    name_check_2 = shared_rooms.loc[shared_rooms["Name"].str.contains(i, na=False)]
    share_check_2 = shared_rooms.loc[shared_rooms["Share with"].str.contains(i, na=False)]
    shared_combine = [name_check_2, share_check_2]
    shared_combined = pd.concat(shared_combine)      
    
#Sort Shared Room applicants with clash and export to CSV    
for i in clash_search: 
         
    clash_check_1 = shared_combined.loc[shared_combined["Share with"].str.contains(i, na=False)]
    clash_check_2 = shared_combined.loc[shared_combined["Not Share With"].str.contains(i, na=False)]
    clash_combine = [clash_check_1, clash_check_2]
    clash_combined = pd.concat(clash_combine)
    export_csv = clash_combined.to_csv(exported_file, mode='a', header=False)

#Duplication entry removal variables
dupe_removal_test = "C:/Users/Gav/Desktop/Accommodation_Manager/Temp/clashes.csv"
without_dupes = "C:/Users/Gav/Desktop/Accommodation_Manager/Exported_Files/clashes_without_dupes_" + date_data + "_" + time_data + ".csv"

#Import and export for duplicate entry removal
clash_test_no_dupes = pd.read_csv(dupe_removal_test, index_col = 0)
clash_test_no_dupes.drop_duplicates(subset=None, inplace=True)
clash_test_no_dupes.to_csv(without_dupes)

#Delete temporary CSV file
os.remove("Temp/clashes.csv")
print("\n-------------------------------------------------\nThe following Accommodation clashes have occurred:\n-------------------------------------------------")
print(clash_test_no_dupes)

#End of program
    