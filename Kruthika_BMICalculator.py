print("===== BMI CALCULATOR =====")

name = input("Enter your name: ")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("\nHello", name)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Category: Normal weight")

elif bmi >= 25 and bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obese")

print("\nThank you for using BMI Calculator")
