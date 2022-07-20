# breakfast between 7:00 and 8:00,
# lunch between 12:00 and 13:00,
# dinner between 18:00 and 19:00.


def main():
    tm = input("What time is it? ")
    print(convert(tm))


def convert(time):
    time = time.strip().split(":")
    hr = int(time[0])
    min = int(time[1])

    if hr == 7 and min in range(0, 60) or hr == 8:
        return "Breakfast time"
    elif hr == 12 and min in range(0, 60) or hr == 13:
        return "Lunch time"
    elif hr == 18 and min in range(0, 60) or hr == 19:
        return "Dinner time"
    else:
        return "Rest time"


if __name__ == "__main__":
    main()
