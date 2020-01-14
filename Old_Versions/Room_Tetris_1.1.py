import numpy as np
import pandas as pd
from datetime import datetime


now = datetime.now()
time_data = now.strftime("%H.%M.%S")
date_data = now.strftime("%d-%m-%Y")

count = 0

data = pd.read_csv("Test_Data.csv")
data2 = pd.read_csv("Test_Data.csv")

print("\nAll Applicants: \n", data)

# dh = data.head()
# print("\nFirst Five Entries: \n", dh)

pa = data['Previous Attendance'].mean()
print("\nPrevious Attendance Average: \n", pa)

toploc = data['Location'].value_counts().head(1)
print("\nLocation with most applicants: \n", toploc)

filename = "C:/Users/Gav/Desktop/Accommodation_Manager/test/export_dataframe_" + date_data + "_" + time_data + ".csv"

export_csv = toploc.to_csv (filename, index = None, header=True)

count_row = data.shape[0] # gives number of row count
# count_col = data.shape[1]  # gives number of column count
print("\nTotal Number of Applicants: \n", count_row)

#---------------------------------

single_rooms = data[data["Type of Room"]=="Single"]
print("\nSingle Rooms:\n\n", single_rooms)

double_rooms = data[data["Type of Room"]=="Double"]
print("\nDouble Rooms:\n\n", double_rooms)

shared_rooms = data[data["Type of Room"]=="Shared"]
# print("\nShared Rooms:\n")
# print(shared_rooms)

filename2 = "C:/Users/Gav/Desktop/Accommodation_Manager/test/shared_rooms_" + date_data + "_" + time_data + ".csv"

export_csv = shared_rooms.to_csv (filename2, index = None, header=True)

shared_no_pref = shared_rooms[shared_rooms["Share with"].isnull()]
print("\nShared Rooms - No preferred Room Mate:\n\n", shared_no_pref)

shared_with_pref = shared_rooms[shared_rooms["Share with"].notnull()]
print("\nShared Rooms - With preferred Room Mate:\n\n", shared_with_pref)

snorers = shared_no_pref.loc[shared_no_pref["Snores or Not"] == "Snores"]
print("\nShared Rooms - No preferred Room Mate - Snores:\n\n", snorers)

light_sleepers = shared_no_pref.loc[shared_no_pref["Snores or Not"] == "Light Sleeper"]
print("\nShared Rooms - N preferred Room Mate - Light Sleepers:\n\n", light_sleepers)

sn_night_owls = snorers.loc[snorers["Nocturnal Habits"] == "Night Owl"]
print("\nShared Rooms - No preferred Room Mate - Snores - Night Owls:\n\n", sn_night_owls)

sn_early_birds = snorers.loc[snorers["Nocturnal Habits"] == "Early Bird"]
print("\nShared Rooms - No preferred Room Mate - Snores - Early Birds:\n\n", sn_early_birds)

ls_night_owls = light_sleepers.loc[light_sleepers["Nocturnal Habits"] == "Night Owl"]
print("\nShared Rooms - No preferred Room Mate - Light Sleepers - Night Owls:\n\n", ls_night_owls)


# while (count > len(ls_night_owls)):
    # ls_night_owls = light_sleepers.loc[light_sleepers["Nocturnal Habits"] == "Night Owl"]
    # count + 1
    # print("\nShared Rooms - No preferred Room Mate - Light Sleepers - Night Owls:\n\n", ls_night_owls)
# else:
    # print("\nNo data available to sort\n")

ls_early_birds = light_sleepers.loc[light_sleepers["Nocturnal Habits"] == "Early Bird"]
print("\nShared Rooms - No preferred Room Mate - Light Sleepers - Early Birds:\n\n", ls_early_birds)

# count = 0

# while (count >= 1):
    # ls_early_birds = light_sleepers.loc[light_sleepers["Nocturnal Habits"] == "Early Bird"]
    # count + 1
    # print("\nShared Rooms - No preferred Room Mate - Light Sleepers - Early Birds:\n\n", ls_early_birds)
# else:
    # print("\nNo data available to sort\n")
    
# dbg = double_rooms.groupby(['Name','Share with']).agg(['count'])
# print("sortee", dbg)

# dbg2 = double_rooms['Previous Attendance'].groupby([double_rooms['Name'], double_rooms['Share with']])
# print("sortee2", dbg2)

# share_match_test = data.where[data["Name"] == ["Share with"]]
# print("\nSharing Couples - Test:\n\n", share_match_test)

# share_match_test = data.equals[data["Name"] == ["Share with"]]
# print("\nSharing Couples - Test:\n\n", share_match_test)

# ------------------------------------------------------------------
# share_match_test = data[data["Name"] == data["Share with"]]
# print("\nSharing Couples - Test:\n\n", share_match_test)

share_match_test = set(data['Name']).intersection(set(data2['Share with']))
print("\nSharing Couples - Test:\n\n", share_match_test)

for i in share_match_test: 
    print("\n", i)

    # share_match_test_2 = data["Share with"].str.match(i)
    # print("\nSharing Couples - Test 2:\n\n", share_match_test_2)
    
    # bb = data["Name"]= data["Share with"].str.find(i)
          
    aa = data.loc[data["Name"].str.contains(i, na=False)]
    bb = data.loc[data["Share with"].str.contains(i, na=False)]
    
    comb = [aa, bb]
    combine = pd.concat(comb)
    
    print("\nSharing Couples - Test 2:\n\n", combine)
    # print(bb)

# for i in share_match_test: 
    # print(i) 

#handy command
data.info()

#doesn't generate an output with Anaconda
data.describe()


