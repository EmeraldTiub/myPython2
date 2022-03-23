# a buncha def's
def convert_in2cm(inches):
    return inches * 2.54
def convert_1b2kg(inches):
    return pounds / 2.2
def convert_cm2in(cm):
    return cm * 2.54
def convert_kg21b(kg):
    return kg * 2.2
# a buncha variables
# part1 of variables
number_ping_pong = eval(input("Enter a number of ping-pong balls: "))
# part2 of variables
height_ping_pong_cm = 4 * number_ping_pong
height_ping_pong_kg  = 2.7 * number_ping_pong / 1000
# part3 of variables
height_in = round(convert_in2cm(height_ping_pong_cm))
weight_1b = round(convert_kg21b(height_ping_pong_kg))
# part4 of variables
feet = height_in // 12
inch = height_in % 12
# two prints
print("if you had", number_ping_pong, "ping pong balls, they would measure")
print(feet, "feet", inch, "inches tall, and weigh", weight_1b, "pounds")
