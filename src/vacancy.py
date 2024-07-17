import json


class Vacancy:
    def __init__(self, name, salary, url, employer):
        name: str
        url: str
        employer: str

        self.name = name
        self.url = url
        self.employer = employer
        self.check_salary(salary)

    def check_salary(self, salary):
        """Проверка корректности указанной ЗП"""
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0

    def __str__(self):
        return (f"Название: {self.name}\nЗарплата от {self.salary_from} до {self.salary_to}\nСсылка: {self.url}\n"
                f"Название компании: {self.employer}")

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from > other.salary_from
        return False

    @classmethod
    def cast_to_object(cls, file):
        """Создание списка объектов класса Вакансия из файла с данными в формате json"""
        vacancies = []
        with open(file, "r") as file:
            data = json.load(file)

        for each in data:
            vacancies.append(Vacancy(name=each['name'], url=each['alternate_url'], employer=each['employer']['name'],
                                     salary=each['salary']))
        return vacancies
