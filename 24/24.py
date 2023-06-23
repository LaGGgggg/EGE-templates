# задача: https://inf-ege.sdamgia.ru/problem?id=27421


with open('24_input_1.txt', 'r') as f:  # "r" - режим чтения. "f" - файл

    result = 0

    for line in f.readlines():  # итерируемся по строкам

        last_symbol = ''
        current_result = 0

        for symbol in line:  # итерируемся по символам в строке

            if symbol == last_symbol:

                result = max(result, current_result)  # максимальный из результатов становиться новым результатом
                last_symbol = ''
                current_result = 0

            else:

                last_symbol = symbol
                current_result += 1

    print(result)


# задача: https://inf-ege.sdamgia.ru/problem?id=27698

with open('24_input_2.txt', 'r') as f:  # "r" - режим чтения. "f" - файл

    result = 0

    for line in f.readlines():  # итерируемся по строкам

        current_result = 0

        for symbol in line:  # итерируемся по символам в строке

            if symbol == 'R':
                current_result += 1

            else:
                result = max(result, current_result)  # максимальный из результатов становиться новым результатом
                current_result = 0

    print(result)


# задача: https://inf-ege.sdamgia.ru/problem?id=35998

with open('24_input_3.txt', 'r') as f:  # "r" - режим чтения. "f" - файл

    result = 0

    for line in f.readlines():  # итерируемся по строкам
        if line.count('A') < 25:
            for symbol in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                """
                rindex - индекс самого правого символа, index - левого
                ("=A=RRA<A>R" "=A=" - этот символ найдёт index, "<A>" - этот символ найдёт rindex)
                """
                result = max(line.rindex(symbol) - line.index(symbol), result)

    print(result)
