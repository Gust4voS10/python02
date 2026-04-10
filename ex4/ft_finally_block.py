class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plants(plant_list: list[str | None]) -> None:
    for plant in plant_list:
        if plant[0] < "A" or plant[0] > "Z":
            raise PlantError(f"Caught PlantError: "
                             f"Invalid plant name to water: '{plant}'")
        else:
            print(f"Watering {plant}: [ok]")


def test_watering_system(plant_list: list[str | None]) -> None:
    try:
        water_plants(plant_list)
    except PlantError as W:
        print(W)
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrot"])
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrot"])
    print("Cleanup always happens, even with errors!")
