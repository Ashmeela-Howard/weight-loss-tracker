def log_meal():
    print("--- Log a meal ---")
    meal_name = input("What did you eat? ")
    calories = float(input("How many calories are in this meal? "))
    carbs = float(input("How many grams of carbs are in this meal? "))
    protein = float(input("How many grams of protein are in this meal? "))
    fat = float(input("How many grams of fat are in this meal?"))
    Meal = {"meal_name": meal_name, "calories": calories, "carbs": carbs, "protein": protein, "fat": fat }
    print("Meal logged: " + meal_name + " | calories: " + str(calories))
    return Meal
log_meal()