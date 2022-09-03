#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


print(f'x | y | z | ¬x | ¬y | ¬z | X ⋁ Y ⋁ Z | ¬(X ⋁ Y ⋁ Z) | ¬X ⋀ ¬Y ⋀ ¬Z')

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            if x == 0: a = 1
            else: a = 0
            if y == 0: b = 1
            else: b = 0
            if z == 0: c = 1
            else: c = 0

            if x == 1 or y == 1 or z == 1: d = 1
            else: d = 0

            if d == 0: e = 1
            else: e = 0

            if a == 0 or b == 0 or c == 0: f = 0
            else: f = 1
            print(f'{x} | {y} | {z} | {a}  | {b}  | {c}  |      {d}    |       {e}      |    {f}')

