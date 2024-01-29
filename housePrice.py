price = int(input("What is price of house? Rs."))
credit_score = int(input("What is your credit score? "))
down_payment = 0

if credit_score > 700 and credit_score < 900:
    down_payment = (price * 10) // 100
else:
    down_payment = (price * 20) // 100

print(f"Down Payment: Rs.{down_payment}")
