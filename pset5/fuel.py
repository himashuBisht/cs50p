def main():

    fraction = input("Fraction: ")
    frac = convert(fraction)
    print(gauge(frac))


def convert(fraction):
    while True:
        try:
            a, b = fraction.split("/")
            a = int(a)
            b = int(b)

            frac = round((a / b) * 100)

            if frac <= 100:

                return frac
            else:
                pass

        except (ZeroDivisionError, ValueError):
            raise


def gauge(percentage):

    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
