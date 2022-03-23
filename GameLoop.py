# define a variable called "keep_going"
keep_going = True
# start of a while loop
while keep_going:
    answer = str(input("Hit [enter] to keep going, any key to exit: "))
    keep_going = (answer == "")
