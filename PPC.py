def convert_in2cm(inches):
    return inches * 2.54
def convert_1b2kg(pounds):
    return pounds / 2.2
height_in = int(input("Enter your height in inches: "))
weight_1b = int(input("Enter your weight in pounds: "))
height_cm = convert_in2cm(height_in)
weight_kg = convert_1b2kg(weight_1b)
ping_pong_tall = round(height_cm / 4)
ping_pong_heavy = round(weight_kg * 1000 / 2.7)
feet = height_in // 12
inch = height_in % 12
print("at", feet, "feet", inch, "inches tall, and", weight_1b, "pounds")
print("you measure", ping_pong_tall, "ping-pong balls tall, and ")
print("you weigh the same as", ping_pong_heavy, "ping-pong balls!")
