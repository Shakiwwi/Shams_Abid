def main():
    """use a dictionary to store each item and how many times it was entered"""
    grocery = {}

    """keep asking for items until the user presses control d"""
    while True:
        try:
            item = input().strip().upper()

            """add the item to the dict or increase its count"""
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1

        except EOFError:
            break

    """print each item sorted alphabetically with its count"""
    for item in sorted(grocery):
        print(f"{grocery[item]} {item}")


main()
