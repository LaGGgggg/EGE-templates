# Тип 2 алгоритм:

[Задание =>](https://inf-ege.sdamgia.ru/problem?id=15939)

### 1. Пишем программу для перебора комбинаций сочитания переменных:

#### Разбор построчно:

Выводим "шапку" таблицы для удобства (просто печатаем названия переменных):
```python
print('x y z w')
```

Перебираем все варианты переменной "x" (0 и 1):
```python
for x in (0, 1):
```

Повторяем тоже самое для остальных переменных (соблюдая табуляцию (tab в теле каждого цикла)):
```python
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
```

Переписываем выражение, которым задаётся логическая функция в конструкции if
(в данной задаче это: "(z ∧ y) ∨ ((x → z ) ≡ (y → w))"):<br>
**Не забываем, что выражение должно быть или истинным (1), или ложным (0),
это написано в последней колонке таблицы значений выражения;
если оно истинно, то просто переписываем выражение, иначе, пишем выражение в конструкции not(<выражение>).**<br>
**Также, для удобного перевода логического выражения на python, привожу таблицу в помощь:**

| знак | python | логическое |
|:----:|:------:|:----------:|
|  ∧   |  and   |     *      |
|  ∨   |   or   |     +      |
|  ¬   |  not   |            |
|  ≡   |   ==   |            |
|  →   |   <=   |            |

```python
if not((z and y) or ((x <= z) == (y <= w))):
```

И добавляем вывод переменных после конструкции if,
они выведутся, если выражение удовлетворяет условиям (истинно (1) или ложно (0))
```python
print(x, y, z, w)
```

В итоге получаем такой код:
```python
print('x y z w')

for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                if not((z and y) or ((x <= z) == (y <= w))):
                    print(x, y, z, w)
```

Результатом его исполнения будет:
```bash
x y z w
0 1 0 0
1 0 0 0
1 0 0 1
1 1 0 1
```

### 2. Анализируем результат программы:

Анализ, обычно, начинается с переменной, которая истинна (1) или ложна (0) во всех строках исходной таблицы значений:

| ??? | ??? | 	???	 | ***???*** | F |
|:---:|:---:|:-----:|:---------:|:-:|
|     |     |       |  ***1***  | 0 |
|  1  |     |       |  ***1***  | 0 |
|  1  |     |   1   |  ***1***  | 0 |

Тут мы можем заметить, что в результате работы программы у нас получилось на строку больше, чем нужно,
берём только те, которые содержат в себе одну переменную, принимающуюю только истину (1)
(так как в исходной таблице значений одна переменная принимет только истину (1)).<br>
**x** y z w<br>
~~0 1 0 0~~<br>
**1** 0 0 0<br>
**1** 0 0 1<br>
**1** 1 0 1<br>

Из полученных данных делаем вывод, что переменная, которая всегда принимает только истину (1) - **x**.<br>
Продолжаем процедуру, аналогично находим столбец, в котором переменная принимает истину (1) в двух случаях
(*важно отметить, что такой столбец уникален, он только **один***).

| ***???*** | ??? | ??? | x | F |
|:---------:|:---:|:---:|:-:|:-:|
|           |     |     | 1 | 0 |
|  ***1***  |     |     | 1 | 0 |
|  ***1***  |     |  1  | 1 | 0 |

x y z **w**<br>
1 0 0 **0**<br>
1 0 0 **1**<br>
1 1 0 **1**<br>

Значит, первый столбец - **w**.<br>
Аналогичными методами приходим к ответу:

| w | z | y | x | F |
|:-:|:-:|:-:|:-:|:-:|
|   |   |   | 1 | 0 |
| 1 |   |   | 1 | 0 |
| 1 |   | 1 | 1 | 0 |

Ответ: **wzyx**.

Нам даже не понадобилось дополнять исходную таблицу значений, но вообще, полностью она выглядит так:

| w | z | y | x | F |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 |

P.S. Методы определения того, какая именно переменная соответствует переменной в таблице могут быть разными,
но все они оснооваются на чистой логике, так что просто чуть-чуть подумайте и всё получится, удачи:)