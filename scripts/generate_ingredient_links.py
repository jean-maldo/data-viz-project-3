import csv

with open('../data/ingredient_links.csv', 'wb') as csvfileout:
    writer = csv.writer(csvfileout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    with open('../data/recipes_nutritional_ingredients.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = reader.next()
        writer.writerow(["source", "target", "recipe", "breakfast", "brunch", "lunch", "dinner", "dessert", "ice cream", "drink", "drinks", "vegan", "vegetarian"])
        for row in reader:
            for i in range(11, len(row) - 1):
                if int(row[i]) != 0:
                    for j in range(i+1, len(row)-1):
                        if int(row[j]) != 0:
                            writer.writerow([header[i], header[j]] + row[0:11])
                            #print(str(header[i]) + " " + str(header[j]))