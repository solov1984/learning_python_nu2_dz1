"""
Описание объекта - холодильника
"""

#Тип str, модель
fridge_model='Bosch KGV36NL1AR'

#Тип str, тип охлаждения
fridge_type_of_cooling='Компрессорный'

#Тип float, вес, кг.
fridge_weight=64.03

#Тип int, объем, л.
fridge_volume=317

#Тип int, количество полок
fridge_racks=4

#Тип bool, наличие морозилки
fridge_freezer=True

print('Объект - холодильник')
print('Модель',fridge_model,'Тип',type(fridge_model))
print('Тип охлаждения',fridge_type_of_cooling,'Тип',type(fridge_type_of_cooling))
print('Вес',fridge_weight,'Тип',type(fridge_weight))
print('Объем',fridge_volume,'Тип',type(fridge_volume))
print('Количество полок',fridge_racks,'Тип',type(fridge_racks))
print('Есть морозилка?',fridge_freezer,'Тип',type(fridge_freezer))


