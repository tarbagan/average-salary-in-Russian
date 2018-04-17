from urllib.request import urlopen
import json
import statistics

minsal = set()
for url in range(2): #pagination. number of vacancies / 100
    page = str(url)
    lnk = "http://opendata.trudvsem.ru/api/v1/vacancies/region/1700000000000/?offset="+page+"&limit=100" #parsing json https://trudvsem.ru
    response = urlopen(lnk)
    data = response.read()
    jsn = json.loads(data)
    for i in jsn["results"]["vacancies"]:
        if (i['vacancy']["salary_min"]) != 0:
            if (i['vacancy']["salary_max"]) != 0:
                minsal.add(((i['vacancy']["salary_min"])+(i['vacancy']["salary_max"]))/2)
            else:
                minsal.add(i['vacancy']["salary_min"])

sal = str(round((statistics.mean(minsal)), 1))
cnt = str(len(minsal))
print ("Средняя зарплата в Туве на основе анализа " + cnt + " вакансий : " + sal + " руб")     
