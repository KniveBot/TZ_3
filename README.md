# TZ_3
If you are just a passerby continue your journey. There is nothing of interest for you here.

## Этот проект создан для соответствия критериям ТЗ 3.
##### Файл, который осуществляет работу программы: test.py
### Результатом этой работы является проект, который:
1) Складывает все целые числа в файлах
2) Осуществляет умножение всех чисел в файле
3) Находит минимальное число в файле
4) Находит максимальное число в файле

### Перед началом проведения данных опираций проводится тест, для оценки верности входных данных(не допускаются форматы ввода: str, bool, float)
### После выполнения программы проводятся тесты на правильность ее выполнения
### Также проводится тест для подсчета времени исполнения программы при нормальном вводе и при увеличении размера входного файла.

![example workflow](https://github.com/KniveBot/TZ_3/actions/workflows/main.yml/badge.svg)

### Пример:
##### В файле:
##### 1 2 3
##### Максимальное:  3

##### В файле:
##### 1 2 3
##### Минимальное:  1

##### В файле:
##### 1 2 3
##### Сумма: 6

##### В файле:
##### 1 2 3
##### Произведение: 6

##### --- 0.0010254383087158203 секунд ---
##### _________________________________________________________________________
##### --------Тесты с увеличением размера файла(чисел в 10 раз больше)---------

##### В файле:
##### 1 2 3 92 28 77 57 28 50 57 62 4 71 70 68 1 57 69 21 27 34 41 92 23 26 27 46 46 36 34
##### Максимальное:  92

##### В файле:
##### 1 2 3 92 28 77 57 28 50 57 62 4 71 70 68 1 57 69 21 27 34 41 92 23 26 27 46 46 36 34
##### Минимальное:  1

##### В файле:
##### 1 2 3 92 28 77 57 28 50 57 62 4 71 70 68 1 57 69 21 27 34 41 92 23 26 27 46 46 36 34
##### Сумма: 1250

##### В файле:
##### 1 2 3 92 28 77 57 28 50 57 62 4 71 70 68 1 57 69 21 27 34 41 92 23 26 27 46 46 36 34
##### Произведение привышает 1000^10. Процесс остановлен.

##### --- 0.0019659996032714844 секунд ---

##### Разница во времени:
##### --- 0.0009405612945556641 секунд ---

Итого реализованно 5 тестов. 4 на коректность работы. 1 на коректность ввода. Также есть проверка поведения программы при увеличении объема файла. И я еще сделал так, чтобы при подсченте произведения, если оно привышает 1000^10(1 000 000 000 000 000 000 000 000 000 000), то питон перестает ее считать(Это сделано, чтобы излишне не нагружать компьютер).

#### Выполнил: Пащенко Николай Александрович ББИ 2003

###### P.S: Автозапуск программы работает
