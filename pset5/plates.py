def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(num):
    # “All vanity plates must start with at least two letters.”
    # For example, AAA222 would be an acceptable …vanity plate; AAA22A would not be acceptable.
    num = list(num)
    c = 0
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if 2 > len(num) or len(num) > 6:
        return False
    for n in num:
        if n in [",", ".", " ","!"]:
            return False
        # The first number used cannot be a ‘0’.
        if n.isdigit():
            c += 1
            if c == 1 and n == "0":
                return False
    # for i in range(len(num)):
    #     if num[i].isdigit():
    #         if not num[i:].isdigit():
    #             return False

    # “Numbers cannot be used in the middle of a plate; they must come at the end.
    # cs50p2 is invalid
    if num[len(num)-1].isdigit() and num[len(num)-2].isalpha():
        return False

    else:
        return True



if __name__ == "__main__":
    main()