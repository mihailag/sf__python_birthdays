# DevOpsHW

Программа для подсчета времени между датами.
На вход подается файл [datafile.py][], содержащий даты рождений сотрудников.
Выводит список сотрудников отсортированный по уменьшению возраста.

По итогам формируется json-документ, содержащий список сотрудников, каждый из которых имеет следующие теги:
1. количество дней с даты рождения сотрудника до текущего числа;
1. возраст (в годах) на момент рождения самого младшего сотрудника;

## Требования
python 3.7 и выше

[datafile.py]: https://github.com/mihailag/sf__python_birthdays/blob/master/datafile.py