my_dict = {'Илья': 1997, 'Анна': 2000, 'Изабелла': 2023}
print(my_dict)
print(my_dict['Анна'])
print(my_dict.get('Тимофей'))
my_dict.update({'Степан' : 2021,
                'Тимофей' : 2019,
                'Эмма': 2025})
print(my_dict)
a = my_dict.pop('Эмма')
print(a)
print(my_dict)

my_set = {1.1,4,5,5,'Home',True}
print(my_set)
print(my_set.add(10))
print(my_set.add((3,3,3)))
print(my_set)
print(my_set.discard(5))
print(my_set)

