bw = 100
height = 173
age = 22
goal = "b"
gender = "m"
priceLimit = 700

if gender == "m":
    calorie_need = 66.47 + (13.75 * bw) + (5.003 * height) - (6.755 * age)
elif gender == "f":
    calorie_need = 655.1 + (9.563 * bw) + (1.850 * height) - (4.676 * age)
else:
    calorie_need = 0

if goal == "b":
    proteinMaxLimit = bw * 2.5                          
    carbMaxLimit = 8 * bw                               
    carbMinLimit = 3 * bw                               
    fatMaxLimit = 1.4 * bw                              
    fatMinLimit = 0.6 * bw                              
    caloriesMaxLimit = calorie_need * 1.4               
    caloriesMinLimit = 0                                

elif goal == "c":
    proteinMaxLimit = bw * 3
    carbMaxLimit = 4.5 * bw
    carbMinLimit = 2 * bw
    fatMaxLimit = 1.1 * bw
    fatMinLimit = 0.7 * bw
    caloriesMaxLimit = calorie_need * 0.9
    caloriesMinLimit = 0

print(proteinMaxLimit," > protein > " ,bw*0.9 )
print(carbMaxLimit, " > carb > ",carbMinLimit)
print(int(fatMaxLimit), " > fat > ",int(fatMinLimit))
print(calorie_need, " > calories > ",1000)

#print(calorie_need)
