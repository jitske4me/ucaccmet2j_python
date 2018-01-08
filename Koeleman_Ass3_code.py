# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:41:31 2018

@author: Jitske
"""

#Seattle,WA,GHCND:US1WAKG0038

import json

with open('precipitation.json') as file:
    info = json.load(file)
    
# format is: [{'datatype': 'PRCP', 'date': '2010-01-01', 
#               'station': 'GHCND:USW00093814', 'value': 0}]        


## Maybe automate: open stations, find seattle and corresponding code 


####
## Part 1
####
    
Seattle_station = []
monthly_prec = 12*[0]  
# Order is: year-month-day

# For all entries in info, check if it's Seattle and add that to a seperate list
for entry in range(len(info)):
    temp = info[entry]['station']
    
    #select all entries for Seattle and make that a list
    if temp == 'GHCND:US1WAKG0038':
        Seattle_station += [info[entry]]
        ## Select the Month, by looking at every entry, then at the key 'date' 
        ## and then taking the month part from the string
        month = int(info[entry]['date'][5:7] )
        ## At loc month-1 (bc index starts at 0), add the precipitation for that day
        monthly_prec[month-1]+= info[entry]['value']

print(monthly_prec)

# Write to a json file        
with open('monthly_prec.json', 'w') as file:
    json.dump(monthly_prec, file) #, indent=4)  


####
## Part 2
####

yearly_prec = sum(monthly_prec)
rel_prec = 12 * [0]

for i in range(len(monthly_prec)):
    rel_prec[i] = round(monthly_prec[i]/yearly_prec, 2)

print(rel_prec)










