grocery={}

while True:
    try:
        order = input("").upper()
        if order in grocery:
            grocery[order]+=1
        else:
            grocery[order] = 1

    except EOFError:
        # grocery_sort =
        for ord  in dict(sorted(grocery.items())):
            print(f"{grocery[ord]} {ord}")
        break
