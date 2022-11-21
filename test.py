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

# import requests
# from bs4 import BeautifulSoup
# import csv

# def write_to_csv(data):
#     with open('cars.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'], data['price'], data['img']])


# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml')
#     page_list = soup.find('div', class_='pages fl').find_all('a')
#     last_page = page_list[-2].text
#     return last_page

# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     cars = soup.find("div", class_="catalog-list").find_all("a", class_="catalog-list-item")
#     # print(cars)
#     for car in cars:
#         try:
#             title = car.find('span', class_="catalog-item-caption").text.strip()
#         except:
#             title = ''

#         try:
#             img = car.find('img', 'catalog-item-cover-img').get('src')
#         except:
#             img=''

#         try:
#             price = car.find("span", class_="catalog-item-price").text
#         except:
#             price = ''
#         data = {'title':title, 
#                 'price':price,
#                 'img':img
#         }
#         write_to_csv(data)

# def main():
#     url_ = 'https://cars.kg/offers'
#     html = get_html(url_)
#     # get_data(html)
#     number = int(get_total_pages(html))
#     i =1
#     while i<= number:
#         print(i)
    
#         url =f'https://cars.kg/offers/{i}'
#         html = get_html(url)
#         number = int(get_total_pages(html))
#         if not BeautifulSoup(html, 'lxml').find('div', class_="catalog-list"):
#             break

#         get_data(html)
#         i += 1
    


# with open('cars.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['title', 'price','img'])
    

# main()


#task parsing
# html = requests.get('https://enter.kg/').text
# soup = BeautifulSoup(html, 'lxml')
# category_list = soup.find('ul', class_="VMmenu")
# print(category_list)

# def find_category(categories, keyword):
#     return categories.find(keyword)
# <ul class="VMmenu" id="VMmenu47_07796"> <li class="VmClose"><div> <a href="/computers">Ноутбуки, Ультрабуки, Гот. решения (2119)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown87"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown87" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/computers/gotovye-resheniya-asus-3_bishkek">Готовые решения ASUS(3)</a></div></li> <li class="VmClose"> </li><li><div><a href="/computers/gotovye-resheniya_bishkek">Готовые решения (18)</a></div></li> <li class="VmClose"> </li><li><div><a href="/computers/noutbuki_bishkek">Ноутбуки (2054)</a></div></li> <li class="VmClose"> </li><li><div><a href="/computers/ultrabuki_bishkek">Ультрабуки (44)</a></div></li> <li class="VmClose"> </li><li><div><a href="/computers/planshetnye-pk_bishkek">Планшетные ПК</a></div></li> <li class="VmClose"> </li><li><div><a href="/computers/elektronnye-knigi_bishkek">Электронные книги (3)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/monitory_bishkek">Мониторы (77)</a> </div></li> <li class="VmClose"><div> <a href="/processory_bishkek">Процессоры (116)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown5"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown5" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/processory_bishkek/processory-amd_bishkek">AMD (14)</a></div></li> <li class="VmClose"> </li><li><div><a href="/processory_bishkek/intel-i3-i5-i7_bishkek">Intel i3, i5, i7, i9 (84)</a></div></li> <li class="VmClose"> </li><li><div><a href="/processory_bishkek/intel-pentium-dual-core_bishkek">INTEL Pentium Dual Core (14)</a></div></li> <li class="VmClose"> </li><li><div><a href="/processory_bishkek/intel-celeron_bishkek">Intel Celeron (4)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/materinskie-platy_bishkek">Материнские платы (75)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown65"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown65" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/materinskie-platy_bishkek/socket-1700_bishkek">socket LGA 1700 (12th Gen) (30)</a></div></li> <li class="VmClose"> </li><li><div><a href="/materinskie-platy_bishkek/socket-1151-v2-8th-gen">socket 1151 V2 (8th &amp; 9th Gen) (18)</a></div></li> <li class="VmClose"> </li><li><div><a href="/materinskie-platy_bishkek/socket-1151_bishkek">socket 1151 (6th &amp; 7th Gen) (7)</a></div></li> <li class="VmClose"> </li><li><div><a href="/materinskie-platy_bishkek/socket-1200_bishkek">socket LGA 1200 (10th &amp; 11th Gen) (18)</a></div></li> <li class="VmClose"> </li><li><div><a href="/materinskie-platy_bishkek/socket-amd">AMD (2)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/operativnaya-pamyat_bishkek">Оперативная память (143)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown66"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown66" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/operativnaya-pamyat_bishkek/ddr-4_bishkek">DDR 4 (112)</a></div></li> <li class="VmClose"> </li><li><div><a href="/operativnaya-pamyat_bishkek/ddr-1_bishkek">DDR 5 (20)</a></div></li> <li class="VmClose"> </li><li><div><a href="/operativnaya-pamyat_bishkek/ddr-3_bishkek">DDR 3 (11)</a></div></li> <li class="VmClose"> </li><li><div><a href="/operativnaya-pamyat_bishkek/ddr-2_bishkek">DDR 2</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/vnutrennie-zhestkie-diski_bishkek">Внутренние жесткие и SSD диски (242)</a> </div></li> <li class="VmClose"><div> <a href="/korpusa_bishkek">Корпуса для ПК (80)</a> </div></li> <li class="VmClose"><div> <a href="/bloki-pitaniya-dlya-pk_bishkek">Блоки питания для ПК (107)</a> </div></li> <li class="VmClose"><div> <a href="/videokarty_bishkek">Видеокарты (70)</a> </div></li> <li class="VmClose"><div> <a href="/diskovody_opticheskie-privody_bishkek">Оптические приводы (4)</a> </div></li> <li class="VmClose"><div> <a href="/sistemy-ohlazhdeniya_bishkek">Системы охлаждения (125)</a> </div></li> <li class="VmClose"><div> <a href="/akustika_kolonki_bishkek">Акустика (колонки) (63)</a> </div></li> <li class="VmClose"><div> <a href="/klaviatury-i-myshki_bishkek">Клавиатуры и мышки (409)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown75"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown75" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/klaviatury-i-myshki_bishkek/myshki_bishkek">Мышки (225)</a></div></li> <li class="VmClose"> </li><li><div><a href="/klaviatury-i-myshki_bishkek/klaviatury_bishkek">Клавиатуры (105)</a></div></li> <li class="VmClose"> </li><li><div><a href="/klaviatury-i-myshki_bishkek/klaviatura-myshka_bishkek">Клавиатура+мышка (30)</a></div></li> <li class="VmClose"> </li><li><div><a href="/klaviatury-i-myshki_bishkek/kovriki-dlya-myshek_bishkek">Коврики для мышек (49)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/printery-skanery-mfu_bishkek">Принтеры, Сканеры, МФУ (41)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown82"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown82" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/printery-skanery-mfu_bishkek/lazernye-printery_bishkek">Лазерные Принтеры (12)</a></div></li> <li class="VmClose"> </li><li><div><a href="/printery-skanery-mfu_bishkek/mfu_bishkek">МФУ (25)</a></div></li> <li class="VmClose"> </li><li><div><a href="/printery-skanery-mfu_bishkek/struynye-printery_bishkek">Струйные Принтеры (1)</a></div></li> <li class="VmClose"> </li><li><div><a href="/printery-skanery-mfu_bishkek/skanery_bishkek">Сканеры (1)</a></div></li> <li class="VmClose"> </li><li><div><a href="/printery-skanery-mfu_bishkek/matrichnye-printery_bishkek">Матричные Принтеры (2)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/tv">Телевизоры и все для них (119)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown310"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown310" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/tv/televizory_bishkek">Телевизоры (42)</a></div></li> <li class="VmClose"> </li><li><div><a href="/tv/krepleniya-dlya-televizorov_bishkek">Крепления для TV/монитора (77)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/sotovye_telefony_bishkek">Мобильные телефоны, смартфоны (21)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown303"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown303" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/sotovye_telefony_bishkek/vse-dlya-smartfonov_bishkek">Все для смартфонов (21)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/vse-dlya-noutbukov_bishkek">Все для ноутбуков (271)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown276"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown276" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/vse-dlya-noutbukov_bishkek/sumki-dlya-noutbukov_bishkek">Сумки и рюкзаки для ноутбуков (58)</a></div></li> <li class="VmClose"> </li><li><div><a href="/vse-dlya-noutbukov_bishkek/nakleyki-dlya-klaviatury_bishkek">Наклейки для клавиатуры (4)</a></div></li> <li class="VmClose"> </li><li><div><a href="/vse-dlya-noutbukov_bishkek/podstavki-s-ohlazhdeniem_bishkek">Подставки с охлаждением (12)</a></div></li> <li class="VmClose"> </li><li><div><a href="/vse-dlya-noutbukov_bishkek/operativnaya-pamyat-dlya-noutbukov_bishkek">Оперативная память для ноутбуков (65)</a></div></li> <li class="VmClose"> </li><li><div><a href="/vse-dlya-noutbukov_bishkek/hdd-dlya-noutbukov_bishkek">HDD для ноутбуков (27)</a></div></li> <li class="VmClose"> </li><li><div><a href="/vse-dlya-noutbukov_bishkek/akkumulyatory-dlya-noutbukov_bishkek">Аккумуляторы для ноутбуков (25)</a></div></li> <li class="VmClose"> </li><li><div><a href="/vse-dlya-noutbukov_bishkek/bloki-pitaniya-dlya-noutbukov_bishkek">Блоки питания для ноутбуков (80)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/vse-dlya-printerov_bishkek">Все для принтеров (416)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown287"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown287" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/vse-dlya-printerov_bishkek/donornye-sistemy_bishkek">Донорные системы</a></div></li> <li class="VmClose"> </li><li><div><a href="/vse-dlya-printerov_bishkek/kartridzhi_bishkek">Картриджи (185)</a></div></li> <li class="VmClose"> </li><li><div><a href="/vse-dlya-printerov_bishkek/rashodnye-materialy_bishkek">Расходные материалы (231)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/vneshnie-zhestkie-diski_bishkek">Внешние жесткие диски (44)</a> </div></li> <li class="VmClose"><div> <a href="/fleshki_bishkek">Флеш-карты USB (флешки) (98)</a> </div></li> <li class="VmClose"><div> <a href="/sd-microsd-card-reader_bishkek">SD, MicroSD, Card Reader (29)</a> </div></li> <li class="VmClose"><div> <a href="/web-kamery_bishkek">WEB камеры (22)</a> </div></li> <li class="VmClose"><div> <a href="/graficheskie-planshety_bishkek">Графические планшеты (7)</a> </div></li> <li class="VmClose"><div> <a href="/naushniki_bishkek">Наушники (169)</a> </div></li> <li class="VmClose"><div> <a href="/programnoe-obespechenie_bishkek">Программное обеспечение (21)</a> </div></li> <li class="VmClose"><div> <a href="/igrovye-ustroystva_bishkek">Игровые устройства (2)</a> </div></li> <li class="VmClose"><div> <a href="/setevoe-oborudovanie_bishkek">Сетевое оборудование (310)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown90"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown90" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/setevoe-oborudovanie_bishkek/wifi_routery_adaptery_bishkek">WiFi роутеры, адаптеры (168)</a></div></li> <li class="VmClose"> </li><li><div><a href="/setevoe-oborudovanie_bishkek/provodnoe-oborudovanie_bishkek">Проводное Оборудование (141)</a></div></li> <li class="VmClose"> </li><li><div><a href="/setevoe-oborudovanie_bishkek/3g-4g-modemy-routery-sot-oper_bishkek">3G 4G модемы (+роутеры) Сот.Опер (1)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/proektory-i-ekrany_bishkek">Проекторы и экраны (15)</a> </div></li> <li class="VmClose"><div> <a href="/telefony-faksy_bishkek">Телефоны, Факсы</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown39"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown39" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/telefony-faksy_bishkek/faksy_bishkek">Факсы</a></div></li> <li class="VmClose"> </li><li><div><a href="/telefony-faksy_bishkek/domashnie_telefony_bishkek">Телефоны</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/perehodniki-shnury-konektory_bishkek">Переходники, шнуры, коннекторы (393)</a> </div></li> <li class="VmClose"><div> <a href="/sistemy-zaschity-pitaniya_bishkek">Системы защиты питания (164)</a> <span class="VmArrowdown"> <svg class="svg" width="10" height="10"> <symbol id="s-crown79"> <polygon points="0,0,6,5,0,10,2,5" fill="white" stroke="orange" stroke-width="0"></polygon> </symbol> <use xlink:href="#s-crown79" x="0" y="0"></use> </svg> </span> </div><ul class="menu" style="display: none;"> <li class="VmClose"> </li><li><div><a href="/sistemy-zaschity-pitaniya_bishkek/аккумуляторы-для-ups">Аккумуляторы для UPS (43)</a></div></li> <li class="VmClose"> </li><li><div><a href="/sistemy-zaschity-pitaniya_bishkek/setevye-filtry_bishkek">Сетевые фильтры (17)</a></div></li> </ul> </li> <li class="VmClose"><div> <a href="/oborudovnie-dlya-ofisa_bishkek">Оборудование для офиса (15)</a> </div></li> <li class="VmClose"><div> <a href="/chistyaschie-sr-va-dlya-tehniki_bishkek">Чистящие ср-ва для техники (9)</a> </div></li> <li class="VmClose"><div> <a href="/usb-haby_bishkek">USB хабы (3)</a> </div></li> <li class="VmClose"><div> <a href="/videoregistratory-dlya-avto_bishkek">Видеорегистраторы для авто (11)</a> </div></li> <li class="VmClose"><div> <a href="/servernoe-oborudovanie_bishkek">Серверное оборудование (135)</a> </div></li> <li class="VmClose"><div> <a href="/instument">Инструменты (68)</a> </div></li> <li class="VmClose"><div> <a href="/zvukovye-karty_bishkek">Звуковые карты (5)</a> </div></li> </ul>
# print(find_category(category_list, 'Ноутбуки'))




"""Спарсить vesti.kg только названия новостей(title) и записать результат в csv файл
"""
import requests
from bs4 import BeautifulSoup
import csv

html = requests.get("https://vesti.kg/").text
soup = BeautifulSoup(html, 'lxml')
for i in soup.find_all('h2'):
    temp = i.find('a').text.strip()
    # print(i.find('a').text.strip())

    with open('title.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow([temp])
        x = str(1)
        

# for i in soup.find_all('h2'):
   
#    

# print(write)   
# ('a').text.strip())
        
        

