parts = ["Sierpień","Nawiedzenie","Ptaki","Manekiny","Traktat o manekinach albo Wtóra Księga Rodzaju","Traktat o manekinach. Ciąg dalszy","Traktat o manekinach. Dokończenie","Nemrod","Pan","Pan Karol","Sklepy cynamonowe","Ulica Krokodyli","Karakony","Wichura","Noc wielkiego sezonu"]
input_name = "input.csv"
output_name = "output.csv"

import random, csv
used = []
def randomNoRepeat(ls):
    global used
    if len(used)==len(ls):
        used = []
    item = ls[random.randint(0, len(ls)-1)]
    while item in used:
        item = ls[random.randint(0, len(ls)-1)]
    used.append(item)
    return item

output = {}

#Read in

f = open(input_name, "r", encoding="utf-8")
with f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        if row[1] == "":
            output[row[0]] = randomNoRepeat(parts)
        else:
            output[row[0]] = row[1]
print(output)

#Write out

with open(output_name, 'w', encoding="UTF-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in output.keys():
            print(data, output[data])
            writer.writerow([data, output[data]])