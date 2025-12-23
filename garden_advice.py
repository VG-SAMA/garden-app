# Garden Advice App
# This script provides gardening advice based on the season and plant type.
# Improvements include refactoring into functions and adding documentation.


# Hardcoded values for the season and plant type
# TODO: Replace these with input() to allow user interaction
season = "summer"
plant_type = "flower"


def get_season_advice(season):
    """
    Return gardening advice based on the given season.

    Args:
        season (str): The current season (e.g. summer, winter)

    Returns:
        str: Gardening advice related to the season
    """
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """
    Return gardening advice based on the plant type.

    Args:
        plant_type (str): Type of plant (e.g. flower, vegetable)

    Returns:
        str: Gardening advice related to the plant type
    """
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def generate_gardening_advice(season, plant_type):
    """
    Generate combined gardening advice based on season and plant type.

    Args:
        season (str): The current season
        plant_type (str): The type of plant

    Returns:
        str: Combined gardening advice
    """
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)
    return advice


# Generate and display the gardening advice
print(generate_gardening_advice(season, plant_type))
