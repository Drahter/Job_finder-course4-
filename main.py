from src.api_classes import HeadHunterAPI
from src.json_maker import JSONSaver
from src.utils import *
from src.vacancy import *


def user_interaction():
    """Функция, отвечающая за взаимодействие пользователя с программой"""
    search_query = input('Введите поисковый запрос: ')
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    min_sal, max_sal = get_salary()

    hh = HeadHunterAPI()
    data = hh.get_vacancies(search_query, 100)

    saver = JSONSaver()
    saver.save_data(data)

    vacancies = Vacancy.cast_to_object(saver.filename)
    vacancies_with_min_max_salary = check_min_max_salary(vacancies, min_sal, max_sal)
    vacancies_with_min_max_salary = get_vac_filtered_by_salary(vacancies_with_min_max_salary)

    if len(vacancies_with_min_max_salary) > top_n:
        for each in range(0, top_n):
            print(f'{vacancies_with_min_max_salary[each]}\n')
    else:
        for each in vacancies_with_min_max_salary:
            print(f'{each}\n')


print('Добрый день!\nДанная программа поможет подобрать интересные вакансии на сайте hh.ru.\n'
      'Сейчас мы уточним все важные для Вас параметры!')

while True:
    user_interaction()
