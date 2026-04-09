def check_temperature(temp_str: str):
    try:
        temp = int(temp_str)

        if temp > 40:
            print(f"Caught input_temperature error: {temp}"
                  f"°C is too hot for plants (max 40°C)\n")
        elif temp < 0:
            print(f"Caught input_temperature error: {temp}"
                  f"°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature is now {temp}°C\n")

    except ValueError:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp_str}'\n")


def test_temperature_input():
    tmp1 = "25"
    print(f"Input data is '{tmp1}'")
    check_temperature(tmp1)
    tmp2 = "abc"
    print(f"Input data is '{tmp2}'")
    check_temperature(tmp2)
    tmp3 = "100"
    print(f"Input data is '{tmp3}'")
    check_temperature(tmp3)
    tmp4 = "-50"
    print(f"Input data is '{tmp4}'")
    check_temperature(tmp4)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
