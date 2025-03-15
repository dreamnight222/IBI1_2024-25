# Pseudocode:
# 1. Prompt user to input weight (kg) and height (m)
# 2. Convert inputs to float for calculation
# 3. Calculate BMI using the formula: BMI = weight / (height^2)
# 4. Compare BMI with thresholds (underweight < 18.5, normal 18.5-30, obese > 30)
# 5. Print the BMI and weight category

# 1. Prompt user for input
weight = float(input("Enter your weight in kg: "))  # 2. Get weight from user
height = float(input("Enter your height in meters: "))  # 2. Get height from user

# 3. Calculate BMI
bmi = weight / (height ** 2)

# 4. Determine weight category
if bmi < 18.5:
    category = "underweight"
elif bmi <= 30:
    category = "normal weight"
else:
    category = "obese"

# 5. Print result
print("Your BMI is " + str(bmi) + ". You are considered " + category + ".")