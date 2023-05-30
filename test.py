with open('book.txt', 'r', encoding='utf-8') as file:
    data = file.read()
print(data)
data_to_find = input("Введите данные для поиска: ")
#  убрать первые фио, тел
data = data.split('\n')[1::]
print(data)