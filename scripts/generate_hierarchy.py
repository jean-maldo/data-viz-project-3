import csv
import json

import json

data = []

#ingredients together in more than or equal to 5 recipes
with open('../project3/data/ingredient-hierarchies/vegan_gte7.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = reader.next()
    
    for row in reader:
        for i in range(0, 2):
            list_item = next((item for item in data if item['ingredient'] == row[i]), None)
            if list_item == None:
                data.append({'ingredient': row[i], 'size': int(row[2]), 'list_ingredients': [row[(i+1) % 2]]})
            else:
                list_item['list_ingredients'].append([row[(i+1) % 2]])
                list_item['size'] += int(row[2])

with open('../project3/data/ingredient-hierarchies/vegan_gte7_hierarchy.json', 'w') as outfile:  
    json.dump(data, outfile)

print len(data)