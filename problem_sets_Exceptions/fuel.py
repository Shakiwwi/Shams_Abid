def get_fraction():
    """keep asking until we get a valid fraction"""
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            """y cant be zero and x cant be bigger than y"""
            if y == 0:
                raise ZeroDivisionError("y cannot be zero")
            if x < 0 or x > y:
                raise ValueError("x must be between 0 and y")

            return x, y

        except (ValueError, ZeroDivisionError):
            pass


def calculate_percentage(x, y):
    """turn the fraction into a rounded percentage"""
    return round((x / y) * 100)


def main():
    x, y = get_fraction()
    percent = calculate_percentage(x, y)

    """show E if almost empty and F if almost full"""
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


main()
