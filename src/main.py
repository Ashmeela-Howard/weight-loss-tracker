from user_profile import get_user_details
from meal_logger import log_meal
from exercise_logger import log_exercise
from daily_summary import daily_summary
user = get_user_details()
meal = log_meal()
exercise = log_exercise()
daily_summary(user, meal, exercise)