input = input("Greeting:").split()
greeting = input[0].lower()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith('h',0,2):
    print("$20")
else:
    print("$100")
