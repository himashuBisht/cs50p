deep = input(">")
deep = deep.lower().strip()

if deep == "forty two" or deep == "forty-two":
    print('Yes')
elif deep == '42':
    print('Yes')
else:
    print('No')
