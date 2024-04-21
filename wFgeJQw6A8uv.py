#replace the variable mekim with the number to be used, this program can take a very long time to run

import math

result = 1
temp = 1
ekim = 1

for i in range (ekim):
    temp = 1
    for i in range(result):
        temp = 1
        for i in range(temp):
            result = result**ekim
        temp = temp**result
        ekim = ekim**temp
    result = result**temp
    ekim = ekim**result

print(result)