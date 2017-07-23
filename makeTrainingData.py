#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

count = 0
f = open('trainingDate100.csv', 'w')
for line in open('./list_person_all_utf8.csv'):
    gender = random.randint(1, 2)
    age = random.randint(10, 60)
    clicked = random.randint(0, 1)
    itemList = line[:-1].split(',')

    if count == 0:
        f.write("age,gender,clicked,title_id\n")
    elif count < 102:
        for item in [age, gender, clicked, itemList[2]]:
            f.write(str(item))
            f.write(",")
        f.write("\n")
    count += 1
f.close()



