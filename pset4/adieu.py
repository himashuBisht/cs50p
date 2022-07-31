import sys
import inflect

p = inflect.engine()
adieu=[]

while True:
    try:
        it=input('Name: ')
        adieu.append(it)
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(adieu)}")
        break
