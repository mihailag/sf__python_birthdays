from datetime import date
import json
import os

data_file='datafile.py'
result_file='birthday_diff.json'
today = date.today()
birthday_dict = {}

def date_diff():
	if os.path.exists(data_file):
		# сохраняем даты рождения и имена сотрудников в словарь
		with open(data_file) as inf:
			for line in inf:
				line = line.strip().split(' = ') 
				birthday_dict[date.fromisoformat(line[1].strip('"'))]=line[0]
		
		# дата рождения самого младшего сотрудника
		birthday_last = sorted(birthday_dict)[-1]
		
		# формируем json-файл содержащий отсортированный по возрасту список сотрудников и тэги:
		# количество дней с даты рождения
		# возраст в годах на момент рождения самого младшего сотрудника
		for birthday_current in sorted(birthday_dict):
			birthday_json = {}
			birthday_json[birthday_dict[birthday_current]] = {
				'days': (today - birthday_current).days,
				'years': ((birthday_last - birthday_current).days)//365
			}
			with open(result_file, 'a') as write_file:
				json.dump(birthday_json, write_file, ensure_ascii=False)
				write_file.write('\n')

	else:
		print ("Файл не найден")

date_diff()
