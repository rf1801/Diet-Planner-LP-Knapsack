from pulp import *
from foodList import *
from personal import *


items = list(protein.keys())


# Create model
m = LpProblem("Knapsack", LpMaximize)

# Variables
x = LpVariable.dicts('x', items, lowBound=0, upBound=2, cat=int)

# Objective
m += sum(protein[i] * x[i] for i in items)


# Constraint of protein limit
m += sum(protein[i] * x[i] for i in items) <= proteinMaxLimit

# Constraint of carb limit
#m += sum(carb[i] * x[i] for i in items) <= carbMaxLimit
m += sum(carb[i] * x[i] for i in items) >= carbMinLimit

# Constraint of fat limit
m += sum(fat[i] * x[i] for i in items) <= fatMaxLimit
#m += sum(fat[i] * x[i] for i in items) >= fatMinLimit

# Constraint of calories limit
#m += sum(calories[i] * x[i] for i in items) <= caloriesMaxLimit
#m += sum(calories[i] * x[i] for i in items) >= caloriesMinLimit

# Constraint of price limit
#m += sum(price[i] * x[i] for i in items) <= priceLimit*(1-comb/100)
m += sum(price[i] * x[i] for i in items) <= priceLimit




# Optimize
m.solve()

# Print the status of the solved LP
#print("Status = %s" % LpStatus[m.status])


print("bodyweight :" ,bw)

totalCost=0
totalCarbs=0
totalProtein=0
totalCalories=0
# Print the value of the variables at the optimum
for i in items:
    if x[i].varValue>0 :
        print("%s = %d" % (x[i].name, x[i].varValue) , "portion (100g)     cost :", round(x[i].varValue*price[i])  ," da" )
        totalCost=totalCost+ x[i].varValue* price[i]
        totalProtein = totalProtein + x[i].varValue * protein[i]
        totalCarbs = totalCarbs + x[i].varValue * carb[i]
        totalCalories = totalCalories + x[i].varValue * calories[i]



# Print the value of the objective
#print("total obj %d" % value(m.objective) ,"grams")
print("total protein %d" % totalProtein ,"grams")
print("total carbs : %d" % totalCarbs ,"grams")
print("total calories : %d" % totalCalories ,"calorie")
print("total price : %d" % totalCost ,"da")
m=0