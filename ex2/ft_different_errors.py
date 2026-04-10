def garden_operations(operention: int) -> None:
    if operention == 0:
        int("ABC")
    elif operention == 1:
        1 / 0
    elif operention == 2:
        open("non_existent_file.txt", "r")
    elif operention == 3:
        print("a" + 1)
    else:
        print("Operation completed successfully")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
