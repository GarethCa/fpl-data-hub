# Dictionary mappings
TEAM_NUMBER_TO_NAME = {
    1: "Arsenal",
    2: "Aston Villa",
    3: "Bournemouth",
    4: "Brentford",
    5: "Brighton",
    6: "Chelsea",
    7: "Crystal Palace",
    8: "Everton",
    9: "Fulham",
    10: "Liverpool",
    11: "Luton",
    12: "Man City",
    13: "Man Utd",
    14: "Newcastle",
    15: "Nottingham Forest",
    16: "Sheffield Utd",
    17: "Spurs",
    18: "West Ham",
    19: "Wolves",
    20: "Burnley",
}

POSITION_TO_NUMBER = {
    "1": "GKP",
    "2": "DEF",
    "3": "MID",
    "4": "FOW",
}


def replace_values(data: dict) -> dict:
    """
    Replaces team numbers with team names and positions with position numbers in the given dictionary.

    Args:
        data (dict): The input dictionary containing team numbers and positions.

    Returns:
        dict: The dictionary with replaced values.
    """
    result = data.copy()

    if "team_id" in result:
        result["team_id"] = TEAM_NUMBER_TO_NAME.get(result.get("team_id"))
        print(result)
    if "position" in result:
        result["position"] = POSITION_TO_NUMBER.get(
            result["position"], result["position"]
        )
    return result
