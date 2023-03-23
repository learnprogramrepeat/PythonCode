#Python
#Demonstrate Using the if/else Statement to Determine Casing

beverages = ['soda' , 'tea', 'water', 'oj']
for beverage in beverages:
    if beverage == 'oj':
        print(beverage.upper())
    else:
        print(beverage.title())
        