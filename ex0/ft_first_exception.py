def input_temperature(temp_str: str) -> int:
    try:
        tmp = int(temp_str)
        print(f"Temperature is now {tmp}°C\n")
        return tmp
    except ValueError:
        print(f"Caught input_temperature error: invalid literal "
              f"for int() with base 10: '{temp_str}'\n")
        return None


def test_temperature() -> None:

    tmp1 = "25"
    print(f"Input data is '{tmp1}'")
    input_temperature(tmp1)

    tmp2 = "abc"
    print(f"Input data is '{tmp2}'")
    input_temperature(tmp2)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
