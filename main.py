# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '108061232.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

target_data = list(filter(lambda item: item['WDSD'] != ('-99.000' or '-999.000'), data))

station_list = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
ans_list = []
output_list = []

for station in station_list:
    final_data = list(filter(lambda item: item['station_id'] == station, target_data))

    if len(target_data) == (0 or 1): 
        ans_list = [station, 'None']
    else :
        MAX = final_data[0]['WDSD']
        MIN = final_data[0]['WDSD']

        for row in final_data:
            if row['WDSD'] > MAX: 
                MAX = row['WDSD']
            elif row['WDSD'] < MIN:
                MIN = row['WDSD']

        max_range = float(MAX) - float(MIN)
        ans_list = [station, max_range]
    output_list.append(ans_list)
# Retrive ten data points from the beginning.

#=======================================


# Part. 4

#=======================================

# Print result

print(output_list)

#========================================