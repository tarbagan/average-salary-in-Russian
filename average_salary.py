"""
Средняя бюджетная зарплата по региону на основе анализа трудовых вакансий
https://github.com/tarbagan/average-salary-in-Russian
Автор: Иргит Валерий
Версия: 0.2
"""
import requests
import json
import statistics

URL = 'http://opendata.trudvsem.ru/api/v1/vacancies/region/1700000000000/?offset=0&limit=1000'


def get_url():
    """Получаем данные"""
    try:
        r = requests.get(URL).text
        return r
    except Exception as e:
        print(e)


if get_url():
    minsal = set()
    jsn = json.loads(get_url())
    data = [x for x in jsn['results']['vacancies']]
    salary_min = [x['vacancy']['salary_min'] for x in data]
    salary_min = [x for x in salary_min if x != 0]
    mean_zp = round(statistics.mean(salary_min))
    count_vac = len(salary_min)
    print(f'Средняя зарплата в Туве на основе анализа {count_vac} вакансий : {mean_zp} рублей')
else:
    print ('Ошибка, данные не получены')
