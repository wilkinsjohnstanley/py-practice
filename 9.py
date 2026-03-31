food = input ("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"What a coincidence, I like {food} as well")
    food = input("What else do you like? (press q to quit conversation) ")
