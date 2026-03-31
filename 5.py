# logical operators = or, and, not
temp = 80
is_hot_and_sweaty = True

if temp > 79 or is_hot_and_sweaty:
    print("I gotta shower when I get home")
else:
    print("What a lovely day") 

if temp >= 80 and is_hot_and_sweaty:
    print("It's hot.")
elif temp <=0 and not is_hot_and_sweaty:
    print("it's cold")