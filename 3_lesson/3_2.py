# list_dict = [{"V": "S001"}, {"V": "S002"},
#              {"VI": "S001"}, {"VI": "S005"},
#              {"VII": " S005 "}, {"V": " S009 "},
#              {"VIII": " S007 "}]

# print(set([list(i.values())[0].strip() for i in list_dict]))
car = {
    1: 'Ford', 2: 'Mustang', 3: 1964}
x = car.items()
print(x)
car[3] = 2018
print(x)
