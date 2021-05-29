"""3. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

my_dict = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}
read_file = open("file.txt", "r")
write_file = open("newfile.txt", "w")

for read_line in read_file:
    key, value = read_line.split(" - ")
    result = f'{my_dict[key].strip()} - {value}'
    write_file.write(result)



