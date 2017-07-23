#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys
import csv

count = 0
f = open('trainingDate100.csv', 'w')
for line in open('./list_person_all_utf8.csv'):
    gender = random.randint(1, 2)
    age = random.randint(10, 60)
    clicked = random.randint(0, 1)
    itemList = line[:-1].split(',')

    if count == 0:
        # f.write("age,gender,clicked,title_id\n")
        f.write("100,3\n")
    elif count < 101:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([age, gender, clicked, int(itemList[2])])
    count += 1
f.close()



