#replace the variable mfkim with the number to be used, this program can take a very long time to run, 

import math

result = 1
temp = 1
fkim = 1

for i in range (fkim):
    temp = 1
    for i in range(result):
        temp = 1
        for i in range(temp):
            result = math.factorial(fkim)
        temp = math.factorial(result)
        fkim = math.factorial(temp)
    result = math.factorial(temp)
    fkim = math.factorial(result)
    
print(result, temp)