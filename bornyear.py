year = ""
while not year.isdigit():
    year = input("В каком году родился А.С. Пушкин? ")

year = int(year)

if year == 1799:
    print("Верно!")
else:
    print("Неверно!")
