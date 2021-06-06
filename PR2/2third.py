def f23(table):
    for i in reversed(range(len(table))):
        if table[i][0] is None:
            del table[i]

    for x in reversed(range(len(table))):
        for n in reversed(range(len(table[x]) - 1)):
            if table[x][n] == table[x][n + 1]:
                del table[x][n]

    for r in table:
        if r[3] == "Не выполнено":
            r[3] = "N"
        else:
            r[3] = "Y"
        r[0] = r[0].split('+7 ')[1]
        r[0] = r[0].replace(' ', '-')
        r[0] = r[0][:10] + '' + r[0][11:]
        buf = float(r[1]) * 100
        buf = int(buf)
        r[1] = str(buf) + '%'

    table.sort(key=lambda table: table[0])

    for z in table:
        z[2] = z[2].split()[2] + " " + list(z[2].split()[0])[0] + "." + z[2].split()[1]

    return table
# table = [[None, None, None, None, None],
#         ["+7 052 135‐97‐74", "0.3", "Антон Ц. Луниди", "Антон Ц. Луниди", "Выполнено"],
#         [None, None, None, None, None],
#         ["+7 487 195‐60‐13", "0.7", "Эдуард Т. Шенянц", "Эдуард Т. Шенянц", "Не выполнено"],
#         ["+7 239 643‐13‐66", "0.2", "Дамир Л. Сочман", "Дамир Л. Сочман", "Выполнено"],
#         ["+7 708 744‐49‐52", "0.1", "Ринат Т. Нуракянц", "Ринат Т. Нуракянц", "Выполнено"]]

# f23(table)
# print(table)
