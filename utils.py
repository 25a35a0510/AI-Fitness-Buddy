def calculate_bmi(weight, height):
    """
    Calculate BMI.
    weight -> kg
    height -> cm
    """
    height = height / 100
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category


def calculate_water(weight):
    """
    Water intake in liters.
    Formula: 35 ml per kg
    """
    water = weight * 35 / 1000
    return round(water, 2)


def calculate_calories(weight, height, age, gender):
    """
    Daily calorie needs using Mifflin-St Jeor Equation.
    """

    if gender == "Male":
        calories = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        calories = (10 * weight) + (6.25 * height) - (5 * age) - 161

    return int(calories)