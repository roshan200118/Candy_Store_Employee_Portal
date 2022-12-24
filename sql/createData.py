import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "candy_retail"
)

mycursor = db.cursor()

import random

candyNamesCountries = ["Canadian","American","Tamil","Chinese","Italian", "Mexican","French"]
candyNamesFirstWord = ["Rock","Jumbo","Goobers","Giant","Large","Small","Tiny","White","Mini","Glimmering","Candy-coated","Shiny","Hot","Rainbow", "Fluffy", "Amazing", "Jelly","Sweet","Carnival", "Spicy", "Extra", "Soft", "Hard", "Red", "Blue", "Pink","Yellow","Purple","Minty", "Popping","Melty","Fresh", "Sweet", "Salty", "Chewy","Tangy", "Golden", "Blinging", "Healthy", "Amazing", "yummy","mouthwatering", "scrumptious",]
candyNamesSecondWord = ["Caramel", "Watermelon", "Jelly", "Butter", "chocolate with nuts","Chocolate", "Cinnamon","Banana","Blue Raspberry","Coconut","Grape","Lemon","Peach","Orange","Marshmallow","Peanut Butter","Mint","Vanilla","Peppermint","Blueberry","Mango","Salty","Spicy","Sour","mixed","assorted", "Multi-sorted", "Multi-pack", "Value-pack", 'tart']
candyNamesThirdWord = ["Gummies", "Salties","Chips" "Bits", "Bites", "Bars", "Pops","Gumdrops","Powder","Balls","Syrup","Gum", "Chews", "Crystals", "Canes", "Lollipops", "Treats", "Sticks", "Rolls", "Strips", "Gushers", "Goobers", "Crunchies", "Jaw-breakers"]

candyNames = candyNamesThirdWord.copy()

companyNames = ["Billy Bonka & The Candy Factory", "Nantha's Bakery", "Roshan's Candy Corp", "Super Duper Candy Inc", "Santa's Factory", "Omnom Treats", "Bon Bon Sweets", "Candy King Corp", "Divine Delights Inc", "Sweets Factory Shop", "Just Candy Corp", "Land Of Sweets Inc"]

for x in range(10):
    candyNamesSecondWord.append('Chocolate')


for i in range(len(candyNames)):
    candyNames[i] = candyNames[i].lower()

def nameGenerator():
    numWords = random.randint(2,4)
    candyName =""
    firstWord=""
    secondWord=""
    thirdWord=""
    fourthWord=""
    if(numWords == 2):
        chooseFirstWord = random.randint(1,3)
        if(chooseFirstWord==1):
            firstWord = random.choice(candyNamesCountries)
        elif(chooseFirstWord==2):
            firstWord = random.choice(candyNamesFirstWord)
        else:
            firstWord = random.choice(candyNamesSecondWord)
        secondWord = random.choice(candyNamesThirdWord)
        candyName = firstWord + " " + secondWord
        # print(candyName)
        if (candyName.lower() not in candyNames):
            candyNames.append(candyName.lower())  
    elif(numWords == 3):
        chooseFirstWord = random.randint(1,3)
        if(chooseFirstWord==1):
            firstWord = random.choice(candyNamesCountries)
        elif(chooseFirstWord==2):
            firstWord = random.choice(candyNamesFirstWord)
        else:
            firstWord = random.choice(candyNamesSecondWord)
        chooseSecondWord = random.randint(2,3)
        if(chooseSecondWord==2):
            secondWord = random.choice(candyNamesFirstWord)
        else:
            secondWord = random.choice(candyNamesSecondWord)
        thirdWord = random.choice(candyNamesThirdWord)
        candyName = firstWord + " " + secondWord + " " + thirdWord
        if (candyName.lower() not in candyNames):
            candyNames.append(candyName.lower()) 
    elif(numWords == 4):
        chooseFirstWord = random.randint(1,3)
        if(chooseFirstWord==1):
            firstWord = random.choice(candyNamesCountries)
        elif(chooseFirstWord==2):
            firstWord = random.choice(candyNamesFirstWord)
        else:
            firstWord = random.choice(candyNamesSecondWord)
        chooseSecondWord = random.randint(2,3)
        if(chooseSecondWord==2):
            secondWord = random.choice(candyNamesFirstWord)
        else:
            secondWord = random.choice(candyNamesSecondWord)
        chooseThirdWord = random.randint(2,3)
        if(chooseThirdWord==2):
            thirdWord = random.choice(candyNamesFirstWord)
        else:
            thirdWord = random.choice(candyNamesSecondWord)
        fourthWord = random.choice(candyNamesThirdWord)
        candyName = firstWord + " " + secondWord + " " + thirdWord+ " " + fourthWord
        if (candyName.lower() not in candyNames):
            candyNames.append(candyName.lower()) 

while (len(candyNames) < 2500):
    nameGenerator()

class Product:
    def __init__(self, productName, productType):
        self.productName = productName.title()
        self.productType = productType.title()

    def __str__(self):
        return f"{self.productName}, {self.productType}"

products = []

for name in candyNames:
    productTypeStr = ""
    if 'hard' in name or 'rock' in name:
        productTypeStr = 'hard candy'
    elif 'gummies' in name or 'chews' in name or 'soft' in name:
        productTypeStr = 'gummies'
    elif 'lollipops' in name:
        productTypeStr = 'lollipops'
    elif 'chocolate' in name:
        productTypeStr = 'chocolate'
    elif 'syrup' in name:
        productTypeStr = 'syrup'
    else:
        productTypeStr = 'candy'
    product = Product(name, productTypeStr)
    products.append(product)


    
# index = 1803
# for index in range(1803, 0, -1):
#     product = products[index]
#     print(index, product)
#     sqlStatment = "UPDATE candy_retail.product SET productName = %s, productType = %s LIMIT %s"
#     mycursor.execute(sqlStatment, (product.productName, product.productType, index))
#     db.commit()

# index = 150
# for index in range(150, 0, -1):
#     supplierName = random.choice(companyNames)
#     print(index, supplierName)
#     sqlStatment =     sqlStatment = "UPDATE candy_retail.shipment SET supplierName = %s LIMIT %s"
#     mycursor.execute(sqlStatment, (supplierName, index))
#     db.commit()



