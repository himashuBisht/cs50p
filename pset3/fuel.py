while True:
    try:
        f = (input("Fraction: ")).split('/')
        a = int(f[0])
        b = int(f[1])
        fuel = round((a/b)*100)
        if fuel>100:
            continue
        else:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        print('Zero division')
    except ValueError:
        if fuel>100:
            print('')

if fuel >= 99:
    print('F')
elif fuel <= 1:
    print('E')
else:
    print(f"{fuel}%")
