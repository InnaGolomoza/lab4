# Зчитуємо вхідні дані
A = input("Введіть рядок A: ")
B = input("Введіть підрядок B: ")

positions = []

# Цикл по рядку A
for i in range(len(A)):
    match = True
    
    # Перевіряємо, чи співпадає підрядок B з частинкою рядка A
    for j in range(len(B)):
        if i + j >= len(A) or A[i + j] != B[j]:
            match = False
            break
    
    # Якщо підрядок B повністю збігається, зберігаємо позицію
    if match:
        positions.append(i + 1)

# Виводимо результат
if positions:
    print("Позиції входження підрядка B у рядок A:", end=' ')
    for pos in positions:
        print(pos, end=' ')
    print()
else:
    print("Підрядок B не знайдено у рядку A. Результат: -1")
