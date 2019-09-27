import math
print ("Объем бензина в галлонах:")
fuel = float(input())
fuel2 = fuel*3.758
barrel = math.ceil(fuel2/19.5)
gasoline = barrel * 20
energy = fuel * 115000
ethanol = round((energy/75700),2)
price = fuel * 3

print ("Объем бензина в литрах:", fuel2)
print ("Количество необходимых баррелей нефти для получения", fuel2, "литров нефти:", barrel, "баррель")
print ("Объем углекислого газа при сжигании в двигателе этого бензина:", gasoline, "фунтов")
print ("Эквивалентый объем этанола:", ethanol, "галлона")
print ("Стоимость:", price, "USD")

print ("Количество людей, которые водят машину в городе:")
people = float(input())
print ("Количество бензина, потраченного в день:")
amount_of_fuel = float(input())
average_consumption = amount_of_fuel / people
fuel_a_day = int(average_consumption * people)
fuel_a_year = int(fuel_a_day * 365)

print ("Количество безина, проданное за день:", average_consumption)
print ("Количество бензина, проданного за день в вашем городе:", fuel_a_day, "литров")
print ("Количество бензина, проданного за год в вашей стране:", fuel_a_year, "литров")


