driving_age = eval(input("what is the legal driving age where you live in? "))
your_age = eval(input("how old are you? "))
if your_age >= driving_age:
    print("You are old enough to drive!")
else:
    print("Sorry, you can drive in", driving_age - your_age, "years.")
