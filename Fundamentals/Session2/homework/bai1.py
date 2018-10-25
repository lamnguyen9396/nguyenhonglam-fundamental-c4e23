height=int(input("your height? ="))
print(height, "cm")
weight=int(input("your weight? ="))
print(weight, "kg")
BMI=weight/((height/100)**2)
print("BMI =",BMI)
if BMI<16:
    print("you are severely underweight")
elif BMI<18.5:
    print("you are underweight")
elif BMI<25:
    print("you are normal")
elif BMI<30:
    print("you are overweight")
else:
    print("you are obese")
