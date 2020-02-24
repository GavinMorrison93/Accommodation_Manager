#--------------------------------------
# Code written by Gavin Morrison - 2019
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
data = pd.read_csv("Test_Data/Test_Data.csv")
data2 = pd.read_csv("Test_Data/Test_Data.csv")

print("\n---------------------------------------------\nROOM TETRIS\n---------------------------------------------")

#Useful Stats.
previous_attendance = data['Previous Attendance'].mean()
previous_attendance_rounded = round(previous_attendance)
print("\nPrevious Attendance Average: ", previous_attendance_rounded)

toploc = data['Location'].value_counts().head(1)
print("\nLocation with most applicants: ", toploc)

count_row = data.shape[0]
print("\nTotal Number of Applicants: ", count_row)

#Variable for sorting application - Room types
single_rooms = data[data["Type of Room"]=="Single"]
double_rooms = data[data["Type of Room"]=="Double"]
shared_rooms = data[data["Type of Room"]=="Shared"]

#Sharers- With and without preferences
shared_no_pref = shared_rooms[shared_rooms["Share with"].isnull()]
shared_with_pref = shared_rooms[shared_rooms["Share with"].notnull()]

#Snorers & Light Sleepers without share preferences 
snorers = shared_no_pref.loc[shared_no_pref["Snores or Not"] == "Snores"]
light_sleepers = shared_no_pref.loc[shared_no_pref["Snores or Not"] == "Light Sleeper"]

#Snorers - Night Owls and  Early Birds
sn_night_owls = snorers.loc[snorers["Nocturnal Habits"] == "Night Owl"]
sn_early_birds = snorers.loc[snorers["Nocturnal Habits"] == "Early Bird"]

#Light Sleepers - Night Owls and  Early Birds
ls_night_owls = light_sleepers.loc[light_sleepers["Nocturnal Habits"] == "Night Owl"]
ls_early_birds = light_sleepers.loc[light_sleepers["Nocturnal Habits"] == "Early Bird"]

#Comparison for sorting loop 
share_match_test = sorted(set(data['Name']).intersection(set(data2['Share with'])))

#Variable for final export
exported_file = "C:/Users/Gav/Desktop/Accommodation_Manager/Exported_Files/my_file_with_dupes.csv"

#Create CSV file for export with header line only
f = open(exported_file, "w", newline='')
writer = csv.DictWriter(
    f, fieldnames=[" ", "Name", "Diet", "Location", "Smoker or Not", "Snores or Not", "Nocturnal Habits", "Previous Attendance", "Type of Room", "Share with", "Not Share With"])
writer.writeheader()
f.close()

#Sort Double Room applicants and export to CSV
for i in share_match_test:       
    name_check_1 = double_rooms.loc[double_rooms["Name"].str.contains(i, na=False)]
    share_check_1 = double_rooms.loc[double_rooms["Share with"].str.contains(i, na=False)]
    combined_1 = [name_check_1, share_check_1]
    combine_concat = pd.concat(combined_1)    
    export_csv = combine_concat.to_csv(exported_file, mode='a', header=False)

#Sort Shared Room applicants and export to CSV    
for i in share_match_test: 
         
    name_check_2 = shared_rooms.loc[shared_rooms["Name"].str.contains(i, na=False)]
    share_check_2 = shared_rooms.loc[shared_rooms["Share with"].str.contains(i, na=False)]
    comb = [name_check_2, share_check_2]
    combined_2 = pd.concat(comb)      
    export_csv = combined_2.to_csv(exported_file, mode='a', header=False)
    
#Other sorted data for export
export_csv = single_rooms.to_csv(exported_file, mode='a', header=False)
export_csv = shared_no_pref.to_csv(exported_file, mode='a', header=False)
export_csv = snorers.to_csv(exported_file, mode='a', header=False)
export_csv = light_sleepers.to_csv(exported_file, mode='a', header=False)
export_csv = sn_night_owls.to_csv(exported_file, mode='a', header=False)
export_csv = sn_early_birds.to_csv(exported_file, mode='a', header=False)
export_csv = ls_night_owls.to_csv(exported_file, mode='a', header=False)
export_csv = ls_early_birds.to_csv(exported_file, mode='a', header=False)

#Duplication entry removal variables
dupe_removal_test = "C:/Users/Gav/Desktop/Accommodation_Manager/Exported_Files/my_file_with_dupes.csv"
without_dupes = "C:/Users/Gav/Desktop/Accommodation_Manager/Exported_Files/couples_test_" + date_data + "_" + time_data + ".csv"

#Import and export for duplicate entry removal
couples_test_no_dupes = pd.read_csv(dupe_removal_test, index_col = 0)
couples_test_no_dupes.drop_duplicates(subset=None, inplace=True)
couples_test_no_dupes.to_csv(without_dupes)

#Delete temporary CSV file
os.remove("Exported_Files/my_file_with_dupes.csv")

print("\n---------------------------------------------\nSorted data successfully exported\n---------------------------------------------")
    
#End of program


