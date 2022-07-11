def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d = d.split("$")
    # $50.00 to ["$","50.00"]
    return float(d[1])


def percent_to_float(p):
    # TODO
    p = p.split("%")
    #15% to ["15", "%"]
    return float(p[0])/100


main()
