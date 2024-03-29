# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:20:33 2023

@author: niran
"""

sun = 4
wind = 0
hail = -8
discount = 0.9

MarkovModel = {
    'sun': [[1/2, 'sun'], [1/2, 'wind']],
    'wind': [[1/2, 'hail'], [1/2, 'sun']],
    'hail': [[1/2, 'hail'], [1/2, 'wind']]
}

values = {
    'sun': 4,
    'wind': 0,
    'hail': -8
}

print("Iteration 0: ", sun, wind, hail)

cnt = 0
while (cnt < 25):
    temp_sun = MarkovModel['sun']
    ans_sun = 0
    for i in temp_sun:
        ans_sun += i[0]*values[i[1]]
    temp_wind = MarkovModel['wind']
    ans_wind = 0
    for i in temp_wind:
        ans_wind += i[0]*values[i[1]]
    temp_hail = MarkovModel['hail']
    ans_hail = 0
    for i in temp_hail:
        ans_hail += i[0]*values[i[1]]
    values['hail'] = hail + discount*ans_hail
    values['sun'] = sun + discount*ans_sun
    values['wind'] = wind + discount*ans_wind
    print("Iteration ", cnt, " ", values['sun'], values['wind'], values['hail'])
    cnt += 1

print(values['sun'], values['wind'], values['hail'])
