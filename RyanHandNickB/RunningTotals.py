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
def running_totals(interation):
    theSum = 0
    for i in range(interation, 0, -1):
        theSum += i
    print theSum

def main():
    running_totals(5)

if __name__ == '__main__':
    main()