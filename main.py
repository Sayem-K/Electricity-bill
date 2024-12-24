units = int(input("Enter the units consumed: "))
if units < 50:
    bill = (units * 2.60) + 25
elif units > 50 and units < 100:
    bill = (units * 3.25) + 35
elif units > 100 and units < 200:
    bill = (units * 5.26) + 45
elif units > 200:
    bill = (units * 8.45) + 75
else:
    bill = "Invalid input"

print("Bill: ", bill)