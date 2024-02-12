current_temperature = int(input("What is today's temperature (in degree celsius)? "))

# if current_temperature > 30:
#     print("It's a hot day!")
# elif current_temperature < 10:
#     print("It's a cold day!")
# else:
#     print("Enjoy Day! It's a good day.")

if current_temperature < 30 and current_temperature > 10:
    print("Enjoy Day! It's a good day.")
elif current_temperature > 30:
    print("It's a hot day!")
else:
    print("It's a cold day!")
