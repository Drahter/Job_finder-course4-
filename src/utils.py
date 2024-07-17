def get_salary():
    """Функция для получения от пользователя диапазона зарплат"""
    salary = input('Введите желаемую зарплату в виде "минимальная зарплата - максимальная зарплата": ')
    try:
        min_salary_str, max_salary_str = salary.split(' - ')
        min_salary = int(min_salary_str)
        max_salary = int(max_salary_str)
        if min_salary > max_salary:
            raise ValueError
        return min_salary, max_salary
    except ValueError:
        print('Диапазон введен неверно! Пожалуйста, введите суммы в виде'
              '"минимальная зарплата - максимальная зарплата"')


def get_vac_filtered_by_salary(vac_list):
    """Функция для сортировки списка объектов класса Вакансия по нижнему порогу зарплат"""
    vac_sorted = sorted(vac_list, key=lambda vac_list: vac_list.salary_from, reverse=True)
    return vac_sorted


def check_min_max_salary(vac_list, min_sal, max_sal):
    """Функция, отсеивающая вакансии, не подходящие под параметры поиска"""
    result = []
    for each in vac_list:
        if min_sal <= each.salary_from <= max_sal and each.salary_to <= max_sal:
            result.append(each)
    return result
