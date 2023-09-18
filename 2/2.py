# задание: https://inf-ege.sdamgia.ru/problem?id=15939

print('x y z w')

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not((z and y) or ((x <= z) == (y <= w))):
                    print(x, y, z, w)


"""
Результат:
x y z w
0 1 0 0
1 0 0 0
1 0 0 1
1 1 0 1
"""
