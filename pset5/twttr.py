def main():
    tweet = input("").strip()
    print(shorten(tweet))


def shorten(word=''):
    knife = ["a", "e", "i", "o", "u"]
    tweet = list(word)
    res = []
    for i in range(len(tweet)):
        if not tweet[i] in knife:
            res.append(tweet[i])
    twttr = "".join(res)

    return f"{twttr}"


if __name__ == "__main__":
    main()


# ================================
# twttr = input("Input:  ").strip()
# import re
# res = re.split('a|e|i|o|u|A|E|I|O|U', twttr)

# rs = "".join(res)
# print(f"Output: {rs}")
