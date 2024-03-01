spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [spicy_food["name"] for spicy_food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        emojis = "🌶" * spicy_food["heat_level"] 
        spicy_food["heat_level"] = emojis
        print (f'{spicy_food["name"]} ({spicy_food["cuisine"]}) | Heat Level: {spicy_food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            heat_level = spicy_food["heat_level"].count("🌶")
            spicy_food["heat_level"] = heat_level
            return spicy_food
    return None


def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if isinstance(spicy_food["heat_level"], str):
            heat_level = len(spicy_food["heat_level"])
        else:
            heat_level = spicy_food["heat_level"]
        if heat_level > 5:
            print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'🌶' * heat_level}")


def get_average_heat_level(spicy_foods):
    total_heat_level = sum(len(spicy_food["heat_level"]) if isinstance(spicy_food["heat_level"], str) else spicy_food["heat_level"] for spicy_food in spicy_foods)
    num_spicy_foods = len(spicy_foods)
    if num_spicy_foods == 0:
        return 0  
    return total_heat_level // num_spicy_foods

def create_spicy_food(spicy_foods, spicy_food):
    for spicy_food_entry in spicy_foods:
        if isinstance(spicy_food_entry['heat_level'], str) and all(char == '🌶' for char in spicy_food_entry['heat_level']):
            spicy_food_entry['heat_level'] = len(spicy_food_entry['heat_level'])
    if isinstance(spicy_food['heat_level'], str) and all(char == '🌶' for char in spicy_food['heat_level']):
        spicy_food['heat_level'] = len(spicy_food['heat_level'])
    spicy_foods.append(spicy_food)
    return spicy_foods
