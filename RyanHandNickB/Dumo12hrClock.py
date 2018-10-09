#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     09-10-2018
# Copyright:   (c) Owner 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
for day in range (24):
    if day <= 12:
        for mm in range (0,60,15):
            print '{:02}:{:02}am'.format(day, mm)
    if day >=13:
        day -= 12
        for mm in range (0,60,15):
            print '{:02}:{:02}pm'.format(day, mm)

