# Викликати дві матриці: А і В;
# Перемножити їх, отримавши матрицю С;
# Визначити середнє значення елементів матриці С.
from random import randint

class Matrix:
    def __init__(self):
        self.A = []
        self.B = []
        self.C = []
        self.length = 0

    def set_data(self, length):
        self.length = length

        for i in range(self.length):
            row = []
            for j in range(self.length):
                row.append(randint(-10, 10))
            self.A.append(row)

        for i in range(self.length):
            row = []
            for j in range(self.length):
                row.append(randint(-10, 10))
            self.B.append(row)

    def multiply(self):
        for i in range(self.length):
            new_row = []
            for j in range(self.length):
                dot_product = 0
                for k in range(self.length):
                    dot_product += self.A[i][k] * self.B[k][j]
                new_row.append(dot_product)
            self.C.append(new_row)

    def get_avarege(self):
        total_sum = 0
        element_count = 0

        for row in self.C:
            for element in row:
                total_sum += element
                element_count += 1

        if element_count == 0: return 0
        return total_sum / element_count


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введіть розмірність квадратних матриць A i B: ")
            length = int(user_input)
            if length <= 0:
                print("Розмір матриці має бути більше 0. Введіть інше число.")
                continue
            break
        except ValueError:
            print("Ви ввели текст замість числа. Введіть натуральне число.")
            
    matrix = Matrix()
    matrix.set_data(length)
    
    print(f"\n{'Матриця А':<{length * 4}}   {'Матриця В'}")
    for i in range(length):
        print(matrix.A[i], "   ", matrix.B[i])
    
    matrix.multiply()
    
    print("\nРезультат множення (Матриця С):")
    for row in matrix.C:
        print(row)
    
    result_avg = matrix.get_avarege()
    print(f"\nСереднє значення елементів матриці С: {result_avg}")
