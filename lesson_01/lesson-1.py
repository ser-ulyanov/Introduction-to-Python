#Задание 1. Выполните упражнения ниже и сверьте результаты с нашим решением. 
# Если вы хотите сохранить скрипты в свой репозиторий, то создайте отдельную папку для них.

my_heigh = 180
print(my_heigh)

#Задание 2. Перезапишите переменную

my_name = "Сергей"
my_name = "Сергей Ульянов"
print(my_name)

#Задание 3. Получите пользовательский ввод

pet_name = input("Как зовут вашего питомца? ")
print("Ваш любимчик - " + pet_name)

#Задание 4. Создание функции
def print_python():
    print("Учу Python!")

print_python()

#Задание 5. Параметризация функции
def print_text(let):
    print(let, end=" ")

print_text('С')
print_text('Т')
print_text('У')
print_text('Д')
print_text('Е')
print_text('Н')
print_text('Т')