thu = 85
fri = 81
sat = 78
sun = 80
mon = 88
tue = 86
wed = 89


sum = thu + fri + sat + sun + mon + tue + wed
average = sum/5

print(average)


temp = [85, 81, 78, 80, 88, 86, 89]
N = len(temp)  # number of data points in temperature array
sum = 0

for i in range(N):
    sum = sum + temp[i]

average = sum/N

print(average)