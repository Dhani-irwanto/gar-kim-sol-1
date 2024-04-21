#replace the variable mmkim with the number to be used, this program can take a very long time to run

import math

result = 1
temp = 1
mkim = 1

for i in range (mkim):
    temp = 1
    for i in range(result):
        temp = 1
        for i in range(temp):
            result = result*mkim
        temp = temp*result
        mkim = mkim*temp
    result = result*temp
    mkim = mkim*result