#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from easygui import *

tank_size = int(integerbox("Please enter the size of your tank(liters):"))
percent = int(enterbox("Please enter the percentage of your current gas(eg:full is 100, half is 50)"))
mileage = int(enterbox("How long can your car run per liter gas(km/l)?"))
distance_next_station = int(enterbox("Please enter how far is the next station(km)?"))

distance_run = int(((tank_size - 5)* percent/100) * mileage)

if distance_run >= distance_next_station:
    msgbox("You can run another " + str(distance_run) + " km. \nThe next station is " + str(distance_next_station) +
           " km away.\nYou can wait for the next station.")
else:
    msgbox("You can run another " + str(distance_run) + " km.\nThe next station is " + str(distance_next_station) +
           " km away.\nYou have to get gas now!")

