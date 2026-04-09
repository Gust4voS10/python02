def garden_operations(growth: str, days: int, file: str, age: int):
    try:
        growth_value = int(growth)
    except ValueError:
        print(f"Caught ValueError: invalid literal "
              f"for int() with base 10: '{growth}'")
    try:
        growth_rate = 10 / days
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        with open(file, "r") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: [Errno 2] No such file or directory: '{file}'")

    try:
        plant_ages = age + days

    except TypeError:
        print('Caught TypeError: can only concatenate str (not "int") to str')


def test_error_types():
    print("=== Testing Different Error Types ===\n")
    print("Testing ValueError...")
    garden_operations("abc", 10, "garden.txt", "rose")
    print("\nTesting ZeroDivisionError...")
    garden_operations(10, 0, "garden.txt", "rose")
    print("\nTesting FileNotFoundError...")
    garden_operations(10, 5, "nonexistent.txt", "rose")
    print("\nTesting KeyError...")
    garden_operations(10, 5, "garden.txt", "sunflower")


if __name__ == "__main__":
    test_error_types()
