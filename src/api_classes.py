import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для создания различных классов, получающих данные от API"""
    @abstractmethod
    def get_response(self, text, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, text, per_page):
        pass


class HeadHunterAPI(AbstractAPI):
    """Класс для взаимодействия с API ресурса HH.ru"""
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_response(self, text: str, per_page: int):
        """Запрос к сервису НН.ру"""
        params = {"text": f"NAME:{text}", "per_page": per_page}
        response = requests.get(self.url, params=params)
        print('Получаем данные с hh.ru...')
        return response

    def get_vacancies(self, text: str, per_page: int):
        """Раскрываем данные из ответа"""
        vacancies = self.get_response(text, per_page).json()["items"]
        return vacancies
