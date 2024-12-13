# method 1

# Weight = int(input("Enter the weight(kg): "))
# Height = int(input("Enter the Height(cm): "))
# Height1 = Height/100
# BMI = (Weight//(Height1**2))

# print("Your BMI is: ",BMI)

# if BMI <= 18.5:
#     print("You are underweight.")
# elif 18.5 < BMI <= 24.9:
#     print("Your are normal.")
# elif 25 < BMI < 29.29:
#     print("You are overweight.")
# else:
#     print("you are obese")



# method 2

def BMI(weight, height):
    return (weight//(height**2))

weight1 = int(input("Enter the weight(kg): "))
height1 = int(input("Enter the height(cm): "))

w= weight1
h = height1/100

bmi= BMI(w,h)
print("your BMI is: ", bmi)

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your are normal.")
elif 25 < bmi < 29.29:
    print("You are overweight.")
else:
    print("you are obese")