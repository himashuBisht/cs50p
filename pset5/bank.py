# input = input("Greeting:").split()

def main():
    greet = input("Greeting:")
    print(value(greet))


def value(greeting):

    g = greeting.split()
    g = g[0].lower()

    if g.startswith("hello"):
        return 0

    elif g.startswith('h',0,2):
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()