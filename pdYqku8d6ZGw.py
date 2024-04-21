#replace the variable kim with the number to be used, this program can take a very long time to run

import math

result = 1
temp = 1
kim = 1

for i in range (kim):
    temp = 1
    for i in range(result):
        temp = 1
        for i in range(temp):
            result = result+kim
        temp = temp+result
        kim = kim+temp
    result = result+temp
    kim = kim+result
    
print(result, temp)