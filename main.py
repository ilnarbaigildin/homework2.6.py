my_dict = {'Ilnar': 1990, 'Elina': 1992, 'Kamila': 2018, 'Oliviya': 2012}
print(my_dict)
print(my_dict['Ilnar'])
my_dict['Fedor'] = 1991
print(my_dict)
my_dict.update({'Katya': 1994, 'Eva': 2024})
print(my_dict)
del my_dict['Ilnar']
print(my_dict)
print(my_dict.get('Ilnar'))


my_set = {1, 5, 'kiwi', 1, 1, 1, 5, 5, 3, 3, 3, (1, 2, 3)}
print(my_set)
my_set.update({2, 'orange'})
print(my_set)
print(my_set.remove(3))
print(my_set)
