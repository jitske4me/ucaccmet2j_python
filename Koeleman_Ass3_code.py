# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:41:31 2018

@author: Jitske
"""

import json

with open('precipitation.json') as file:
    info = json.load(file)
    
# format stations: Seattle,WA,GHCND:US1WAKG0038
    
# format data: [{'datatype': 'PRCP', 'date': '2010-01-01', 
#               'station': 'GHCND:USW00093814', 'value': 0}]        

station_info = []
with open('stations.csv') as file:
    for line in file:
        line = line.strip('\n')
        line = line.split(',')
        station_info += [line]

station1 = []
station2 = []
station3 = []
station4 = []

monthly_prec1 = 12*[0]  
monthly_prec2 = 12*[0]
monthly_prec3 = 12*[0]
monthly_prec4 = 12*[0]
# Order is: year-month-day


my_dict = {}
for entry in range(1,len(station_info)):
    my_dict[station_info[entry][0]] = {
            'station':station_info[entry][2], 
            'state':station_info[entry][1]}

print(my_dict)

# For all entries in info, check if it's Seattle and add that to a seperate list
for entry in range(len(info)):
    temp = info[entry]['station'] ## select station code
    month = int(info[entry]['date'][5:7]) ## Select the Month, by looking at 
                ## every entry, then at the key 'date' and then 
                ## taking the month part from the string 
            
    if temp == station_info[1][2]:
        station1 += [info[entry]]
        ## At loc month-1 (bc index starts at 0), add the precipitation for that day
        monthly_prec1[month-1]+= info[entry]['value']    
    
    #select all entries for Seattle and make that a list (Seattle,WA,GHCND:US1WAKG0038)
    if temp == station_info[2][2]:
        station2 += [info[entry]]
        monthly_prec2[month-1]+= info[entry]['value']   

    if temp == station_info[3][2]:
        station3 += [info[entry]]
        monthly_prec3[month-1]+= info[entry]['value']   
    
    if temp == station_info[4][2]:
        station4 += [info[entry]]
        monthly_prec4[month-1]+= info[entry]['value']   

my_dict[station_info[1][0]]['totalMonthlyPrecipitation'] = monthly_prec1
my_dict[station_info[2][0]]['totalMonthlyPrecipitation'] = monthly_prec2
my_dict[station_info[3][0]]['totalMonthlyPrecipitation'] = monthly_prec3 
my_dict[station_info[4][0]]['totalMonthlyPrecipitation'] = monthly_prec4

print(my_dict)


monthly_prec = [monthly_prec1,monthly_prec2,monthly_prec3,monthly_prec4]


## Yearly precipitation per city 
yearly_prec = [sum(monthly_prec1),sum(monthly_prec2),sum(monthly_prec3),sum(monthly_prec4)]
total_prec = sum(yearly_prec)
   
rel_monthly_prec = [12*[0], 12*[0], 12*[0], 12*[0]]

for i in range(len(monthly_prec)):
    for j in range(len(monthly_prec[i])):
        rel_monthly_prec[i][j] = round(monthly_prec[i][j]/yearly_prec[i], 2)


## Calculate relative yearly prec and store in dict 
## Also store other vars in dic
count = 0
for entry in my_dict:
    my_dict[entry]['relativeMonthlyPrecipitation'] = rel_monthly_prec[count]
    my_dict[entry]['totalYearlyPrecipitation'] = yearly_prec[count]
    my_dict[entry]['relativeYearlyPrecipitation'] = round(yearly_prec[count]/total_prec,2)

    count += 1    
    

print(my_dict)

# Write to a json file        
with open('results.json', 'w') as file:
    json.dump(my_dict, file, indent=4)  

