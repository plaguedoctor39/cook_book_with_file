def get_list_to_buy():
    with open('cook_book.txt', encoding='utf8') as f:
        cook_book = {}
        i = 0
        ingredient_name = []
        for line in f:
            line_list = line.split()
            if len(line_list) != 0 and line_list[0].isalpha() and i == 0:
                cook_book[' '.join(line_list)] = []
                current_dish = ' '.join(line_list)
            elif len(line_list) == 1 and line_list[0].isdigit():
                i = int(line_list[0])
            elif len(line_list) > 1:
                line_list = list(filter(lambda a: a != '|', line_list))
                for digit in line_list:
                    if not digit.isdigit():
                        ingredient_name.append(digit)
                    else:
                        cook_book[current_dish].append({'ingredient_name': ' '.join(ingredient_name),
                                                        'quantity': digit,
                                                        'measure': line_list[-1] + '.'})
                        ingredient_name = []
                        break
                i -= 1
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_list_to_buy()
    cook_book['Фахитос']
    for dish in cook_book:
        if dish in dishes:
            current_dish = cook_book[dish]
            for ingredient in current_dish:
                current_ingredient = ingredient['ingredient_name']

                # print(current_ingredient)
                if current_ingredient in shop_list:
                    shop_list[current_ingredient] = {'measure': ingredient['measure'],
                                                     'quantity': int(ingredient['quantity']) + int(ingredient['quantity'])}
                else:
                    shop_list[current_ingredient] = {'measure': ingredient['measure'],
                                                     'quantity': int(ingredient['quantity'])}
        else:
            pass
    for ingredient in shop_list.values():
        ingredient['quantity'] *= person_count
    return shop_list


def runner():
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
    print(shop_list)


runner()
