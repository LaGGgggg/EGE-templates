# задача: https://inf-ege.sdamgia.ru/problem?id=7454

for i in range(1000, 9999):

    i_str = str(i)

    part_1_sum = int(i_str[0]) + int(i_str[1])
    part_2_sum = int(i_str[2]) + int(i_str[3])

    if part_1_sum > part_2_sum:
        result = str(part_1_sum) + str(part_2_sum)

    else:
        result = str(part_2_sum) + str(part_1_sum)

    if result == '1311':

        print(i)

        break
