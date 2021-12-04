import csv
import math

with open("data.csv",newline="") as f:
    reader = csv.reader(f)
    file_data=list(reader)

data = file_data[0]

#mean
def mean(data):
    n = len(data)
    tot = 0

    for x in data:
        tot+=x

    mean = tot/n

    return mean

#square

square_list = []

mean = mean(data)

for x in data:
    a = int(x)-mean
    a = a**2
    square_list.append(a)

#sum

sum_data = 0

for x in square_list:
    sum+=x

#devide
result = sum/len(data)

#deviation
standerd_deviation = marh.sqrt(result)

#print

print(standerd_deviation)