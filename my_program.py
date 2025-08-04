print("BMI calculator")
a = float(input("Please enter the value of your weight in kilograms: "))
b = float(input("Please enter the value of your height in meters: "))
bmi = a / (b * b)
if 0 < bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. The value is very low, which means you are underweight")
elif 18.4 < bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}. The value is intermediate, which means you are normal")
elif 24.8 < bmi < 30:
    print(f"Your BMI is {bmi:.2f}. The value is slightly higher, which means you are overweight")
elif 29.9 < bmi < 34.9:
    print(f"Your BMI is {bmi:.2f}. This value is high, which means you are obese")
elif 34.8 < bmi < 50:
    print(f"Your BMI is {bmi:.2f}. This value is very high, which means you are extremely obese")
else:
    print("Error!")
    print("Possible troubleshooting tips:")
    print("1) Entered weight or height are not defined in kilograms or meter")
    print("2) Entered weight or height are not in 'value only' format. Entered value should consists of digits only")
    print("3) Entered value is a negative integer")
    print("Please Re-enter the values")
