year = ""
while not year.isdigit():
    year = input("В каком году родился А.С. Пушкин? ")

year = int(year)

if year == 1799:
    born_day = input("Введите день рождения А.С. Пушкина (ДД.ММ): ")
    if born_day == "06.06":
        print("Верно!")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")
