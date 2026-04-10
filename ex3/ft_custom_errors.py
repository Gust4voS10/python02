class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def erro(plant: str, tank_water: int) -> None:
    if plant == "tomato":
        raise PlantError(f"Caught PlantError: The {plant} plant is wilting!")
    if tank_water < 5:
        raise WaterError("Caught WaterError: Not enough water in the tank!")


def Test() -> None:
    try:
        plant: str = "tomato"
        tank: int = 5
        erro(plant, tank)
    except PlantError as p:
        print("Testing PlantError...")
        print(p)
    try:
        erro("carrot", 2)
    except WaterError as w:
        print("\nTesting WaterError...")
        print(w)
    try:
        erro(plant, 5)
    except GardenError as g:
        print("\nTesting catching all garden errors...")
        print(g)
    try:
        erro("carrot", 2)
    except GardenError as g:
        print(g)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    Test()
