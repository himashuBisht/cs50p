#sol1
import re
twttr = input("Input:  ").strip()

res = re.split('a|e|i|o|u|A|E|I|O|U', twttr)

rs = "".join(res)
print(f"Output: {rs}")



# sol2

twttr = input("Input:  ").strip()
tweet =  list(twttr)
res =[]

for i in range(len(tweet)):
    if not tweet[i].lower() in ['a','e','i','o','u']:
        res.append(tweet[i])

twttr = ''.join(res)
print(f"Output: {twttr}")
