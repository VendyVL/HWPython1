#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Что это за абракадабра?

print(f'x | y | z | ¬x | ¬y | ¬z | X ⋁ Y ⋁ Z | ¬(X ⋁ Y ⋁ Z) | ¬X ⋀ ¬Y ⋀ ¬Z')

for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            print(f'{x} | {y} | {z} | {~x} | {~y} | {~z} |     {x|y|z}     |     {~(x|y|z)}       |   {~x&~y&~z}')

# Где оно берёт -2 вот в чём вопрос.