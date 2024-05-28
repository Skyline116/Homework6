my_dict = {'Олеся': 123456789, 'Дмитрий': 987654321, 'Максим': 543216789 }
print(my_dict)
print(my_dict['Олеся'])
print(my_dict.get('Иван'))
my_dict.update({'Альберт': 324,
                'Ирина': 543})
a = my_dict.pop('Ирина')
print(a)
print(my_dict)


my_set = {'1', '1', 8, 8, True, True}
print(my_set)
my_set.update({7, 9})
my_set.remove(9)
print(my_set)