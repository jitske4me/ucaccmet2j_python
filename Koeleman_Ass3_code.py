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


Seattle_station = []
month_prec = []

for entry in range(len(info)):
    temp = info[entry]['station']
    
    #select all entries for Seattle and make that a list and make a list with month-precipitation
    if temp == 'GHCND:US1WAKG0038':
        Seattle_station += [info[entry]]
   

  
monthly_prec = 12*[0]    
for entry in range(len(Seattle_station)):
    month = int(Seattle_station[entry]['date'][5:7] )
    monthly_prec[month-1]+= Seattle_station[entry]['value']
    

print(monthly_prec)
        
    
    
#year-month-day











