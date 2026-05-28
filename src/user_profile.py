def get_user_details():
    print("Welcome to your Weight Loss Tracker!")
    print("Lets set up your profile.")
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    weight = float(input("What is your current weight in Kg? "))
    height = float(input("What is your current height in cm? "))
    goal_weight = float(input("What is your goal weight in Kg? "))
    user = {"name": name, "age": age, "weight": weight, "height": height, "goal_weight": goal_weight}
    print("Thanks " + name + "! Your profile has been successfully created.")
    return user