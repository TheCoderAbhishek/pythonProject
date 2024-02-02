user_name = input("What is your name? ")

len_name = len(user_name)

if 3 < len_name < 50:
    print("Name looks good!")
elif len_name < 3:
    print("Name must be 3 characters long.")
else:
    print("Name have maximum 50 characters.")
