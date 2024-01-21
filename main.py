import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
contacts_list_new = list()
contacts_list_new.append(contacts_list[0])

# №1
for i in range(1, len(contacts_list)):
    fio = '/'.join(contacts_list[i][0:3])
    fio_2 = fio.replace('//', ' ').replace('/', ' ')
    contacts_list_new.append(fio_2.split(' ')[0:3] + contacts_list[i][3:5])


# №2
for z in range(1, len(contacts_list)):
    pattern = r"(\+7|8)\s*\(*(495)\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d+)\s*\s*\(*([доб.]*)\s*(\d*)\)*"
    substitution = r"+7(\2)\3-\4-\5 \6\7"
    number_new = re.sub(pattern, substitution, contacts_list[z][5])
    contacts_list_new[z].append(number_new.rstrip())
    contacts_list_new[z].append(contacts_list[z][6])

# №3
contacts_list_new_group = list()
for i in contacts_list_new:
    count = 0
    for z in range(0, len(contacts_list_new_group)):
        if (i[0] == contacts_list_new_group[z][0] and i[1] == contacts_list_new_group[z][1] and
                i[2] == contacts_list_new_group[z][2]) or i[2] == '':
            break
        else:
            count += 1
    if count == len(contacts_list_new_group):
        contacts_list_new_group.append(i)
    else:
        if i[2] != '':
            contacts_list_new_group[count][2] = i[2]
        if i[3] != '':
            contacts_list_new_group[count][3] = i[3]
        if i[4] != '':
            contacts_list_new_group[count][4] = i[4]
        if i[5] != '':
            contacts_list_new_group[count][5] = i[5]
        if i[6] != '':
            contacts_list_new_group[count][6] = i[6]


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list_new_group)
