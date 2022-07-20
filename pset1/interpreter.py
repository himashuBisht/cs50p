input = input(">").strip()

n = input.split(" ")
x = float(n[0])
y = float(n[2])

if n[1] == "+":
    print(f"{(x+y):.1f}")

elif n[1] == "-":
    print(f"{(x-y):.1f}")

elif n[1] == "*":
    print(f"{(x*y):.1f}")

elif n[1] == "/":
    print(f"{(x/y):.1f}")
