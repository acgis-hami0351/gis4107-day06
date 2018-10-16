#-------------------------------------------------------------------------------
# Name:        RunningTotalsStrange.py
# Purpose:
#
# Author:      Nick and Ryan
#
# Created:     14/10/2018
# Copyright:   (c) Nick 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    test_strange_sum(4)
    test_strange_sum(5)
    test_strange_sum(0)

def strange_sum(number):
    a_list = list(range(1,(number + 1),1))
    b_list = list(range(number, 0, -1))
    float_a_list = [float(integer) for integer in a_list]
    float_b_list = [float(integer) for integer in b_list]
    division_list = [a/b for a,b in zip(float_a_list,float_b_list)]
    print sum(division_list)


def test_strange_sum(test_number):
    strange_sum(test_number)

if __name__ == '__main__':
    main()










