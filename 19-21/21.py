# Задание: https://inf-ege.sdamgia.ru/problem?id=33100

def f(s1, s2, m):
    """
    s1 - первая куча
    s2 - вторая куча
    m - количество оставшихся ходов
    """

    # Проверка на выигрыш
    if s1 + s2 >= 45:
        # Победа, если ход первого игрока
        return m % 2 == 0

    # Проверка на проигрыш (закончились ходы)
    if m == 0:
        return 0

    # -1 ход, нужно для дальнейших подсчётов
    m -= 1

    # Все возможные следующие ходы игрока
    h = [
        f(s1 + 1, s2, m),
        f(s1, s2 + 1, m),
        f(s1 * 3, s2, m),
        f(s1, s2 * 3, m),
    ]

    # any - есть выиграшная стратегия
    # all - гарантированно при всех возможных ходах
    if m % 2 == 0:
        # Второй игрок
        return any(h)

    else:
        # Первый игрок
        return all(h)


print([s for s in range(1, 41) if not f(4, s, 2) and f(4, s, 4)])
