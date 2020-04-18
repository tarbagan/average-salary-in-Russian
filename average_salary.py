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
    for i in jsn['results']['vacancies']:
        if (i['vacancy']['salary_min']) != 0:
            if (i['vacancy']['salary_max']) != 0:
                minsal.add(((i['vacancy']['salary_min']) + (i['vacancy']['salary_max'])) / 2)
            else:
                minsal.add(i['vacancy']['salary_min'])

    sal = str(round((statistics.mean(minsal)), 1))
    cnt = str(len(minsal))
    print(f'Средняя зарплата в Туве на основе анализа {cnt} вакансий : {sal} рублей')

