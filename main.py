import os
from pprint import pprint

path = os.path.join(os.getcwd(), 'dishes.txt')

with open(path, encoding='utf-8') as file:
    number_of_iterations = 1
    for lines in file:
        dish_name = lines.strip()
        count_ingredients = int(file.readline().strip())
        my_list = []
        for ing in range(count_ingredients):
            ing_list = list(file.readline().strip().split('|'))
            my_list.append(ing_list)

        count = 0
        for i in my_list:
            for k in i:
                count += 1

        elements_ingredients = int(count / count_ingredients)
        i = 0
        dish_structure = []
        while i < count_ingredients:
            dish_composition = {}
            c = 0
            while c < elements_ingredients:
                if c == 0:
                    dish_composition.setdefault('ingredient_name', my_list[i][c])
                if c == 1:
                    dish_composition.setdefault('quantity', my_list[i][c])
                if c == 2:
                    dish_composition.setdefault('measure', my_list[i][c])
                c += 1
            dish_structure.append(dish_composition)
            i += 1
        if number_of_iterations == 1:
            cook_book = {}
            cook_book.setdefault(dish_name, dish_structure)
        else:
            cook_book.setdefault(dish_name, dish_structure)
        file.readline()
        number_of_iterations += 1
    count = 1
    for k, v in cook_book.items():
        print(f'{count}. Наименование блюда: {k.upper()}')
        print(f'Состав: ')
        for i in v:
            print(f'\t Наименование ингредиента: {i["ingredient_name"].strip().upper()}. ', end='')
            print(f'Количество: {i["quantity"].strip()} {i["measure"].strip()}')
        count += 1
    print()


def get_shop_list_by_dishes(list_of_dishes, count_person=1):
    ing_dict = {}
    for dish in list_of_dishes:
        if dish in cook_book.keys():
            for ing in cook_book[dish]:
                my_list = list(ing)
                my_list.remove('ingredient_name')
                my_dict = dict.fromkeys(my_list)
                for k, v in my_dict.items():
                    for key, val in ing.items():
                        if k == key:
                            if key == 'quantity':
                                val = int(val) * count_person
                            my_dict[k] = val
                if len(ing_dict) == 0:
                    ing_dict[ing['ingredient_name']] = my_dict
                elif len(ing_dict) > 0:
                    if ing['ingredient_name'] not in ing_dict:
                        ing_dict[ing['ingredient_name']] = my_dict
                    else:
                        ing_dict[ing['ingredient_name']]['quantity'] += my_dict['quantity']

    for k, v in ing_dict.items():
        print(k, v)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
