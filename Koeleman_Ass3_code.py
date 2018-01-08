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


## to do: open stations, find seattle and corresponding code 


import json

with open('precipitation.json') as file:
    info = json.load(file)
    
Seattle_station = []
monthly_prec = 12*[0]  

for entry in range(len(info)):
    temp = info[entry]['station']
    
    #select all entries for Seattle and make that a list and make a list with month-precipitation
    if temp == 'GHCND:US1WAKG0038':
        Seattle_station += [info[entry]]
        month = int(info[entry]['date'][5:7] )
        monthly_prec[month-1]+= info[entry]['value']

print(monthly_prec)

#Write to a json file        
with open('monthly_prec.json', 'w') as file:
    json.dump(monthly_prec, file) #, indent=4)  



#year-month-day











