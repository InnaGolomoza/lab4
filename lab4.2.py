ferz = input("Введіть координати ферзя: ")

# Перевірка правильності введених координат
if len(ferz) != 2 or not ferz[0].isalpha() or not ferz[1].isdigit():
    print("Некоректні координати. Введіть їх у шаховому форматі.")
else:
    # Визначаємо рядок та стовпець ферзя на шаховій дошці
    column = ord(ferz[0]) - ord('a')
    row = 8 - int(ferz[1])

    # Створюємо шахову дошку та заповнюємо її крапками
    board = [['.' for i in range(8)] for i in range(8)]

    # Позначаємо клітинку, де стоїть ферзь, буквою 'Q'
    board[row][column] = 'Q'

    # Позначаємо клітинки, які б'є ферзь, символами '*'
    for i in range(8):
        for j in range(8):
            if i == row or j == column or abs(i - row) == abs(j - column):
                if board[i][j] != 'Q':
                    board[i][j] = '*'

    # Виводимо шахову дошку на екран
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print()

