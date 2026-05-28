def log_exercise():
    print("--- Log an Exercise ---")
    exercise_name = input("What part of the body did you exercise? ")
    exercise_duration = float(input("How long did you exercise for? (in minutes) "))
    print("Exercise types: walking, pilates, squats, running, hiit, rowing, etc.")
    exercise_type = input("What type of exercise was it? ")
    if exercise_type == "walking":
        met = 2.5
    elif exercise_type == "pilates":
        met = 3
    elif exercise_type == "squats":
        met = 5
    elif exercise_type == "running":
        met = 8
    elif exercise_type == "hiit":
        met = 12
    elif exercise_type == "rowing":
        met = 12
    else:
        met = 5
    weight = float(input("What is your weight? (in kg) "))
    duration_in_minutes = exercise_duration / 60
    calories_burned = met * weight * duration_in_minutes
    print("Calories burned: " + str(calories_burned))
    exercise = {"exercise_name": exercise_name, "exercise_duration": exercise_duration, "calories_burned": calories_burned}
    return exercise
log_exercise()
