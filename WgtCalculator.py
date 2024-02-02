user_name = input("What is your name? ")

weight = float(input("Weight: "))
unit_of_weight = input("(L)bs or (K)gs: ")

unit_of_weight_capital = unit_of_weight.capitalize()

if unit_of_weight_capital == 'L':
    weight = weight / 2.205
    print(f"Hi {user_name}, your weight is {weight} kgs.")

elif unit_of_weight_capital == 'K':
    weight = weight * 2.205
    print(f"Hi {user_name}, your weight is {weight} lbs.")
else:
    print("Please enter valid mass unit!")
