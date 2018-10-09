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
# While
x = 0
while x <= 4:
    x += 1
    if x == 2: continue
    print x
else:
    print "Loop done."

for i in [1,2,3,4]:
    if i == 2: continue
    if i == 3: break
    print i
else:
    print "loop done"