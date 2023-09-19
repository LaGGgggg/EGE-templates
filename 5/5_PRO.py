# задача: https://inf-ege.sdamgia.ru/problem?id=15791

for i in range(1, 1000):

    i_bin_str = str(bin(i))[2:]

    for _ in range(2):
        i_bin_str += str(sum([int(j) for j in i_bin_str]) % 2)

    if (result := int(i_bin_str, 2)) > 97:

        print(result)

        break
