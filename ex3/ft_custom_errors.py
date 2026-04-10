class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def erro(plant: str, tank_water: int) -> None:
    if plant[0] < "A" or plant[0] > "Z":
        raise PlantError(f"Caught PlantError: The {plant} plant is wilting!")
    if tank_water < 5:
        raise WaterError("Caught WaterError: Not enough water in the tank!")


def Test(plant: str, tank_water: int) -> None:
    try:
        erro(plant, tank_water)
    except GardenError as g:
        print(g)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    Test("tomato", 5)
    print("\nTesting WaterError...")
    Test("Lettuce", 3)
    print("\nTesting catching all garden errors...")
    Test("carrot", 5)
    Test("Carrots", 3)
    print("\nAll custom error types work correctly!")
