## Смотри сначала [guide_EZ](guide_EZ)

Единственное отличие [5_EZ](5_EZ.py) от [5_PRO](5_PRO.py) состоит в более сложной конструкции:<br>

*5_EZ.py:*
```python
for _ in range(2):

    summ = 0

    for j in i_bin_str:
        summ += int(j)

    i_bin_str += str(summ % 2)
```

*5_PRO.py:*

```python
for _ in range(2):
    i_bin_str += str(sum([int(j) for j in i_bin_str]) % 2)
```

Результат выполнения конструкций идентичен, но вторая пишется в одну строку.<br>

Разберём по элементам:

```python
[int(j) for j in i_bin_str]
```
Это просто цикл в виде list comprehensions, на выходе получаем список из целочисленных значений строки.

```python
sum([int(j) for j in i_bin_str]) % 2
```
Вычисляем сумму элементов списка с помощью `sum` и получаем остаток от её деления на 2.

```python
i_bin_str += str(sum([int(j) for j in i_bin_str]) % 2)
```

Ну и переводим остаток в строковый тип данных, затем прибавляем эту строку к изначальной строке (которую обрабатывали).
