"""1) Мурат с друзья на выходных решил собратся и пойти в ночной клуб.
Но в ночной клуб пропускают только тех, кому 17+.
Мурату - 24 лет, Эржану - 21 лет, Чынгызу - 24 лет, Алтынай - 17 лет, Асеме - 16 лет.
Напишите программу которая определяет кого пустить в ночной клуб а кого нет. (работа со словарем)
"""
# Friends = {"Murat": 24, "Erjan": 21, "Chingiz":24,"Altytai":17, "Asema":16}
# print("Могут входить: " )
# for k, v in Friends.items():
#   if v >= 17:
#     print(k)

    


"""
2) Дан словарь а, значениями, которого являются словари,
измените словарь 'а' таким образом, чтобы значения внутреннего словаря стали 
внешними значениями
a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
Вывод:
{'a': 32, 'b': 36, 'c': 37, 'd': 21}
"""

# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# b = dict()
# for k, v in a.items():
#     for value in v.values():
#         b[k]= value
# print(b)


"""
3) Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
"""
# a = {"бананы":24, "ананас":5, "яблоки":16, "груши":7}
# for k, v in list(a.items()):
#     if v%2==0:
#         a.pop(k)
# print(a)
"""
4) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
"""
# a = {1:34, 2:45, 3:56}
# b = 0
# for v in a.values():
#     b += v
# print(b)
"""
5) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.
"""
# a = {}
# for i in range(1,11):
#     a[i] = i*i
# print(a)
    

"""
6) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
"""
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# for k, v in list(my_dict.items()):
#     for value in v.values():
#         my_dict[k] = value
# print(my_dict)
"""
7) Дан словарь dict_. Отсортируйте словарь по значениям в порядке уменьшения.
Новые элементы занесите в словарь sorted_dict

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}

Вывод:
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = {}





""""""
# 8) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то запринтите исключение с текстом "Сумма не может быть отрицательной!"
""""""
# a = int(input("Введите число: "))
# if a >= 0:
#     print(f"У вас есть {a} сом")
# else:
#     print("Сумма не может быть отрицательной!")
"""



# 7) Дан словарь dict_. Отсортируйте словарь по значениям в порядке уменьшения.
# Новые элементы занесите в словарь sorted_dict

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}

# Вывод:
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# for k, v in dict_.items():
#     a = sorted(v)
#     sorted_dict[k] = 
# print(sorted_dict)


# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# a = 0
# for k, v in dict_.items():


# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k, v in dict1.items():
#     for value in v.values():
#         print()
# print(dict2)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {}
# a[k] = "even" if v%2 == 0 else a[k]="odd" for k, v in dict_.items():
# print(a)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list1 = [i for i in string_.split()]
# list_ = [num for num in list1 if num.isdigit()]
# print(list_)

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict = {key:k for key, value in dict_.items() for k, v in value.values if v == max(v)}
# print(new_dict)


#15
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_= {key:v for key, value in my_dict.items() for k, v in value.values()}
# print(dict_)


# string = "happy birthday!"
# list_ = [i for i in string]
# # list_ = [i for i in list1 if i != " " and i != "!"]
# # print(list_) 
# print(list_)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list_ = [int(v) for key, value in dict_.items() for k, v in value.values()]
# print(list_)


# 3 
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1/num2)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

#4
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1+num2)
# except ValueError:
#     print("Введите число!")

#5
# dict_ = {'key1': 'value1', 'key2': 'value2'}
# try:
#     print(dict_["key3"])
# except KeyError:
#     print("Нет такого ключа!")

#6
# list_ = [1, 4, 9, 16, 25, 36]
# try:
#     print(list_[6])
# except IndexError:
#     print("Нет такого элемента!")

#7
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError("Доступ запрещён")
# except(ValueError):
#     print("Введён некорректный возраст")
# else:
#     print("Спасибо")
# finally:
#     print("До свидания!")

#8
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1/num2)
# except(ZeroDivisionError, ValueError):
#     print("Произошла ошибка!")

#9
# cash = int(input())
# try:
#     if cash < 0:
#         raise ValueError
# except(ValueError):
#     print("Сумма не может быть отрицательной!")
# else:
#     print(cash)

#10
# try:
#     inp1 = input()
#     inp2 = input()
#     res = int(inp1) + int(inp2)
# except ValueError:
#     res = inp1 + inp2
# finally:
#     print(res)

# try:
#     inp1 = input().split()
#     list_ = []
#     for i in inp1:
#         int(i)
#         list_.append(i)
# except ValueError:
#     print("Данный элемент не является числом!")


# dict_ = {'first': 1, 'second': 2, 'third': 3}

# a = {key:"even" 
#     if v%2==0 
#     else key:"odd"
#     for key, v in dict_.items()}
# print(a)  

# dict_ = {i:list(range(i+1)) for i in range(1,6)}
# print(dict_)




# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {key.replace("i",""):key.count('i') for key, value in dict1.items() }
# print(dict2)

#3
# import requests
# from bs4 import BeautifulSoup

# html = requests.get("https://www.wikipedia.org/").text
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find('div', class_="central-featured-lang lang6").find("strong").text)
# print(soup.find('div', class_="central-featured-lang lang6").find("small").text)


#4
# import requests
# from bs4 import BeautifulSoup


# def getTitle(url):
#     html = requests.get(url)
#     soup = BeautifulSoup(html.text, 'lxml')
#     res = soup.find('h1')
#     if res != None:
#         return res 
#     else:
#         res = "Title could not be found"
#         return res

# print(getTitle('http://www.example.com/'))

#pip3 install -r requirments.txt #(внутри requirments есть requestsб bs4)

import requests
from bs4 import BeautifulSoup
import csv

def write_to_csv(data):
    with open('cars.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['img']])


def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div', class_='pages fl').find_all('a')
    last_page = page_list[-2].text
    return last_page

def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    cars = soup.find("div", class_="catalog-list").find_all("a", class_="catalog-list-item")
    # print(cars)
    for car in cars:
        try:
            title = car.find('span', class_="catalog-item-caption").text.strip()
        except:
            title = ''

        try:
            img = car.find('img', 'catalog-item-cover-img').get('src')
        except:
            img=''

        try:
            price = car.find("span", class_="catalog-item-price").text
        except:
            price = ''
        data = {'title':title, 
                'price':price,
                'img':img
        }
        write_to_csv(data)

def main():
    url_ = 'https://cars.kg/offers'
    html = get_html(url_)
    # get_data(html)
    number = int(get_total_pages(html))
    i =1
    while i<= number:
        print(i)
    
        url =f'https://cars.kg/offers/{i}'
        html = get_html(url)
        number = int(get_total_pages(html))
        if not BeautifulSoup(html, 'lxml').find('div', class_="catalog-list"):
            break

        get_data(html)
        i += 1
    


with open('cars.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'price','img'])
    

main()


