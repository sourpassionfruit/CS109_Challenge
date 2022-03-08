import csv

# first step: import data
file = open("TrainingDataTrial.csv")
reader = csv.reader(file)
header = next(reader)
data = []
for row in reader:
    data.append(row)


# train naive bayes model
total = 0
y1Count = 0
successX1Y1 = 0
successX2Y1 = 0
successX1Y0 = 0
successX2Y0 = 0
for person in data:
    total += 1
    if person[0] == "1":
        y1Count += 1
        if person[1] == "1":
            successX1Y1 += 1
        if person[2] == "1":
            successX2Y1 += 1
    if person[0] == "0":
        if person[1] == "1":
            successX1Y0 += 1
        if person[2] == "1":
            successX2Y0 += 1



# MLE estimates for X1
print("This table is MLE for X1 and Y")
dictX1 = {0: [0, ((total - y1Count) - successX1Y0) / float(total - y1Count), successX1Y0 / float(total - y1Count)], 1: [1, (y1Count - successX1Y1) / float(y1Count), successX1Y1 / float(y1Count)]}
print ("{:<10} {:<10} {:<10}".format('Y','X1 = 0 MLE','X1 = 1 MLE'))
for key, value in dictX1.items():
    y, x1, x0 = value
    print ("{:<10} {:<10} {:<10}".format(y, x1, x0))

print("This table is MLE for X2 and Y")
# MLE estimates for X2
dictX2 = {0: [0, ((total - y1Count) - successX2Y0) / float(total - y1Count), successX2Y0 / float(total - y1Count)], 1: [1, (y1Count - successX2Y1) / float(y1Count), successX2Y1 / float(y1Count)]}
print ("{:<10} {:<10} {:<10}".format('Y','X2 = 0 MLE','X2 = 1 MLE'))
for key, value in dictX2.items():
    y, x1, x0 = value
    print ("{:<10} {:<10} {:<10}".format(y, x1, x0))


# sample data: someone who is a women and born poor, predict outcome
prob0 = float(total - y1Count) / total * dictX1.get(0)[1] * dictX2.get(0)[1]
prob1 = float(y1Count) / total * dictX1.get(1)[1] * dictX2.get(1)[1]
print("If Y = 0, prob is", prob0)
print("If Y = 1, prob is", prob1)
if prob0 > prob1:
    print("We predict Y = 0, the person will be poor")
else:
    print("We predict Y = 1, the person will be rich")