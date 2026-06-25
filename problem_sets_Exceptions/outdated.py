months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


def parse_date(date_string):

    if "/" in date_string:  # try slash format like 9/8/1636
        parts = date_string.split("/")
        if len(parts) != 3:
            raise ValueError("not a valid slash date")
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

    elif "," in date_string:  # try written format like September 8 1636
        parts = date_string.replace(",", "").split()
        if len(parts) != 3:
            raise ValueError("not a valid written date")
        if parts[0] not in months:
            raise ValueError("month name is not valid")
        month = months.index(parts[0]) + 1
        day = int(parts[1])
        year = int(parts[2])

    else:
        raise ValueError("date format is not recognized")

    if not (1 <= month <= 12):  # make sure month is realistic
        raise ValueError("month must be between 1 and 12")
    if not (1 <= day <= 31):  # make sure day is realistic
        raise ValueError("day must be between 1 and 31")

    return year, month, day


def main():
    while True:
        try:
            date_string = input("Date: ").strip()
            year, month, day = parse_date(date_string)
            print(f"{year:04}-{month:02}-{day:02}")
            break
        except ValueError:
            pass


main()