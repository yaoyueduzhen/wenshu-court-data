import csv


# 读取csv至字典
csvRead = open("电池爆炸.csv", "r")
reader = csv.reader(csvRead)

fileHeader = []
data = []
id = []

for item in reader:
    print(item[11])
    print(item[12])
    print(item[13])
    print(item[14])
    print(item[15])
    print('\n\n')