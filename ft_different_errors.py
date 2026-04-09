def garden_operations(growth: str, days: str, file: str, plant: str):
    try:
        growth_value = int(growth)
        days_value = int(days)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        try:
            growth_value / days_value
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
            try:
                file = open(file, "r")
            except FileNotFoundError:
                print(f"Caught FileNotFoundError: No such file '{file}'")
            try:
                plants = {"rose": 5, "tulip": 3, "daisy": 7}
                print(plants[plant])
            except KeyError:
                print(f"Caught KeyError: 'missing{plant}'")


def test_error_types():
    print("=== Testing Different Error Types ===\n")
    print("Testing ValueError...")
    garden_operations("1", "10", "garden.txt", "rose")
    print("\nTesting ZeroDivisionError...")
    garden_operations("10", "0", "garden.txt", "rose")
    print("\nTesting FileNotFoundError...")
    garden_operations("10", "5", "nonexistent.txt", "rose")
    print("\nTesting KeyError...")
    garden_operations("10", "5", "garden.txt", "sunflower")


if __name__ == "__main__":
    test_error_types()
