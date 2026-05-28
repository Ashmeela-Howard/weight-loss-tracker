def daily_summary(user, meal, exercise):
    bmr = 10 * user["weight"] + 6.25 * user["height"] - 5 * user["age"] -161
    total_in = meal["calories"]
    total_out = exercise["calories_burned"] + bmr
    net = total_in - total_out
    print("\n=============================")
    print("         Daily Summary")
    print("=============================")
    print("Name: " + user["name"])
    print("Calories in: " + str(total_in))
    print("BMR (calories burned at rest): " + str(round(bmr)))
    print("Exercise calories burned: " + str(exercise["calories_burned"]))
    print("Total calories out: " + str(round(total_out)))
    print("Net calories: " + str(round(net)))
    if net < 0:
        print("You are in a calorie DEFICIT. Great Work!")
    else:
        print("You are in a calorie SURPLUS remember your goal!")