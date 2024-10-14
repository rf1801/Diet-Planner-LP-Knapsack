# Protein content per 100 grams
protein = {
    "Chicken breast": 31,
    "Eggs": 13,
    "Beef (lean cuts)": 0,
    "Salmon": 0,
    "Cow milk": 3.2,
    "Banana": 1.0,
    "Oatmeal": 2.5,
    "Peanuts": 25.8,
    "Almonds": 21.1,
    "Peanut Butter": 24.9,
    "Potatoes": 2.0,
    "Pasta":5,
}

# Carbohydrate content per 100 grams
carb = {
    "Chicken breast": 0.1,  # Negligible to minimal amounts (less than 1 gram)
    "Eggs": 0.5,  # Less than 1 gram
    "Beef (lean cuts)": 0.1,  # Negligible to minimal amounts (less than 1 gram)
    "Salmon": 0,  # Negligible to minimal amounts (less than 1 gram)
    "Cow milk": 4.7,
    "Banana": 22.0,
    "Oatmeal": 12.0,
    "Peanuts": 16.1,
    "Almonds": 21.6,
    "Peanut Butter": 20.0,
    "Potatoes": 17.5,
    "Pasta":30
}

# Fat content per 100 grams
fat = {
    "Chicken breast": 3.6,
    "Eggs": 10,
    "Beef (lean cuts)": 10,  # Varies depending on the leanness of the cut
    "Salmon": 13,
    "Cow milk": 3.6,
    "Banana": 0.2,
    "Oatmeal": 1.0,
    "Peanuts": 49.2,
    "Almonds": 49.4,
    "Peanut Butter": 50.0,
    "Potatoes": 0.2,
    "Pasta":1
}

price = {
    "Chicken breast": 100,
    "Eggs": 40,
    "Beef (lean cuts)": 250,
    "Salmon": 350,
    "Cow milk": 10,
    "Banana": 40,
    "Oatmeal": 60,
    "Peanuts": 5000,
    "Almonds": 250,
    "Peanut Butter": 80,
    "Potatoes": 5,
    "Pasta":8
}

# Caloric content in 100-gram servings

calories = {
    "Chicken breast": 165,
    "Eggs": 143,
    "Beef (lean cuts)": 250,  # Varies based on the cut and leanness
    "Salmon": 208,  # Approximate for raw salmon fillet
    "Cow milk": 42,  # Approximate for whole cow's milk
    "Banana": 96,  # Approximate for a medium-sized banana
    "Oatmeal": 71,  # Varies based on the type and preparation
    "Peanuts": 570,  # Approximate for dry roasted peanuts, unsalted
    "Almonds": 575,  # Approximate for dry roasted almonds, unsalted
    "Peanut Butter": 588,  # Approximate for smooth peanut butter, unsalted
    "Potatoes": 77,  # Approximate for baked potatoes with skin
    "Pasta":150
}

def addfood(name, protein_val, fat_val, carbs_val, calories_val,price_val):
    # Adding the food to the protein dictionary
    protein[name] = protein_val

    # Adding the food to the fat dictionary
    fat[name] = fat_val

    # Adding the food to the carb dictionary
    carb[name] = carbs_val

    # Adding the food to the calories dictionary
    calories[name] = calories_val

    price[name]=price_val


import pandas as pd

addfood('whey',23,0,1.5,121,300)
addfood('mass',23,2,70,374,326)
addfood('tuna',30,9,0,200,100)

#print(protein)

df=pd.read_csv("C:/Users/raouf/Documents/0data/336_foods.csv")
#print(df.head())
print(df.iloc[0])