name = input("\n>camelCase:  ").strip()
name = list(name)

snake = []

for n in name:
    if n.isupper():
        snake.append("_")
    snake.append(n)
snake_case = "".join(snake).lower()

print(f">snake_case: {snake_case}")
