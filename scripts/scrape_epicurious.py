#import the library used to query a website
import urllib2#

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import csv

domain="http://www.epicurious.com"

file = 'data_scrape_test.csv' # file to read from
out_file = 'recipes_with_servings.csv' # file to write to

with open('recipes_nutritional6.csv', 'wb') as csvfileout:
    writer = csv.writer(csvfileout, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    with open('epi_r2.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # variables for fields read in
            title_row = row[0]
            
            title_row = title_row.strip(' \t\n\r')
            
            title_row = " ".join(title_row.split())
            
            recipe_to_find = title_row
            recipe_parsed = recipe_to_find.replace(' ', '%20')
            recipe_parsed = recipe_parsed.replace(',', '%2C')
            recipe_parsed = recipe_parsed.replace('/', '%2F')

            try:
                #enter epicurious search url
                #print title_row
                recipe_search = domain + "/search/" + recipe_parsed + "?content=recipe"
                #print recipe_search
                #Query the website and return the html for the seach page
                page = urllib2.urlopen(recipe_search)
                
                #Parse the html of the search page
                soup = BeautifulSoup(page, 'html.parser')

                #find the link to the recipe
                right_recipe=soup.find('a', title=title_row)

                if right_recipe:
                    #print right_recipe['href']
                    #Query the website with the link for the recipe
                    try:
                        page_recipe = urllib2.urlopen(domain + right_recipe['href'])
                        #Parse the html for the recipe
                        soup_recipe = BeautifulSoup(page_recipe, 'html.parser')

                        #Find the number of calories
                        nutrition_info=soup_recipe.find('div', class_="edaman-nutrition")
                        
                        if nutrition_info:
                            #Find the number of calories
                            right_cals=soup_recipe.find('span', itemprop="calories")

                            if right_cals:
                                #parse string to get the number
                                cals = int(filter(str.isdigit, str(right_cals.getText())))
                                row[2] = cals
                            else:
                                row[2] = "No cals data"

                            #Find the number of protein
                            right_protein=soup_recipe.find('span', itemprop="proteinContent")

                            if right_protein:
                                protein_string = right_protein.getText()
                                #parse string to get the number
                                protein = int(protein_string[:protein_string.index('g')])
                                protein_percentage = int(protein_string[protein_string.index('(') + 1:protein_string.index('%')])
                                row[3] = protein
                                row.append(protein_percentage)
                            else:
                                row[3] = "No protein data"
                                row.append("No protein data")
                            
                            #Find the number of fat
                            right_fat=soup_recipe.find('span', itemprop="fatContent")

                            if right_fat:
                                fat_string = right_fat.getText()
                                #parse string to get the number
                                fat = int(fat_string[:fat_string.index('g')])
                                fat_percentage = int(fat_string[fat_string.index('(') + 1:fat_string.index('%')])
                                row[4] = fat
                                row.append(fat_percentage)
                            else:
                                row[4] = "No fat data"
                                row.append("No fat data")
                                
                            #Find the number of sodium
                            right_sodium=soup_recipe.find('span', itemprop="sodiumContent")

                            if right_sodium:
                                sodium_string = right_sodium.getText()
                                #parse string to get the number
                                sodium = int(sodium_string[:sodium_string.index('mg')])
                                sodium_percentage = int(sodium_string[sodium_string.index('(') + 1:sodium_string.index('%')])
                                row[5] = sodium
                                row.append(sodium_percentage)
                            else:
                                row[5] = "No sodium data"
                                row.append("No sodium data")
                            
                            #Find the number of carbs
                            right_carbs=soup_recipe.find('span', itemprop="carbohydrateContent")
                            
                            if right_carbs:
                                carbs_string = right_carbs.getText()
                                #parse string to get the number
                                carbs = int(carbs_string[:carbs_string.index('g')])
                                carbs_percentage = int(carbs_string[carbs_string.index('(') + 1:carbs_string.index('%')])
                                row.append(carbs)
                                row.append(carbs_percentage)
                            else:
                                row.append("No carbs data")
                                row.append("No carbs data")
                            
                            #Find the number of saturated fat
                            right_sat_fat=soup_recipe.find('span', itemprop="saturatedFatContent")
                            
                            if right_sat_fat:
                                sat_fat_string = right_sat_fat.getText()
                                #parse string to get the number
                                sat_fat = int(sat_fat_string[:sat_fat_string.index('g')])
                                sat_fat_percentage = int(sat_fat_string[sat_fat_string.index('(') + 1:sat_fat_string.index('%')])
                                row.append(sat_fat)
                                row.append(sat_fat_percentage)
                            else:
                                row.append("No sat fat data")
                                row.append("No sat fat data")
                            
                            #Find the number of fiber
                            right_fiber=soup_recipe.find('span', itemprop="fiberContent")
                            
                            if right_fiber:
                                fiber_string = right_fiber.getText()
                                #parse string to get the number
                                fiber = int(fiber_string[:fiber_string.index('g')])
                                fiber_percentage = int(fiber_string[fiber_string.index('(') + 1:fiber_string.index('%')])
                                row.append(fiber)
                                row.append(fiber_percentage)
                            else:
                                row.append("No fiber data")
                                row.append("No fiber data")
                            
                            #Find the number of cholesterol
                            right_cholesterol=soup_recipe.find('span', itemprop="cholesterolContent")
                            
                            if right_cholesterol:
                                cholesterol_string = right_cholesterol.getText()
                                #parse string to get the number
                                cholesterol = int(cholesterol_string[:cholesterol_string.index('m')])
                                cholesterol_percentage = int(cholesterol_string[cholesterol_string.index('(') + 1:cholesterol_string.index('%')])
                                row.append(cholesterol)
                                row.append(cholesterol_percentage)
                            else:
                                row.append("No cholesterol data")
                                row.append("No cholesterol data")
                            
                        else:
                            row[2] = "No cals data"
                            row[3] = "No protein data"
                            row[4] = "No fat data"
                            row[5] = "No sodium data"
                            row.append("No protein data")
                            row.append("No fat data")
                            row.append("No sodium data")
                            row.append("No carbs data")
                            row.append("No carbs data")
                            row.append("No sat fat data")
                            row.append("No sat fat data")
                            row.append("No fiber data")
                            row.append("No fiber data")
                            row.append("No cholesterol data")
                            row.append("No cholesterol data")
                            
                        row.append(domain + right_recipe['href'])
                    except urllib2.HTTPError, e:
                        row[2] = "Invalid Link"
                        row[3] = "Invalid Link"
                        row[4] = "Invalid Link"
                        row[5] = "Invalid Link"
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append("Invalid Link")
                        row.append(domain + right_recipe['href'])
                        print e
                    
                    
                else:
                    row[2] = "No recipe"
                    row[3] = "No recipe"
                    row[4] = "No recipe"
                    row[5] = "No recipe"
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append("No recipe")
                    row.append(recipe_search)
                    
                writer.writerow(row)
                #print row[0] + " " + str(row[2]) + " " + str(row[3])
            except urllib2.HTTPError, e:
                row[2] = "Invalid Search"
                row[3] = "Invalid Search"
                row[4] = "Invalid Search"
                row[5] = "Invalid Search"
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append("Invalid Search")
                row.append(recipe_search)
                writer.writerow(row)
                #print row[0] + " " + str(row[2]) + " " + str(row[3])
                print e