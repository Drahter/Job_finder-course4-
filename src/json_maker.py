import json
from abc import ABC, abstractmethod


class File(ABC):
    """Абстрактный класс, шаблон для различных классов для работы с разными форматами файлов"""
    @abstractmethod
    def save_data(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(File):
    """Класс для работы с файлами в формате JSON"""
    def __init__(self, file_name="vacancies.json"):
        self.filename = f"data/{file_name}"

    def save_data(self, vacancies):
        """Функция для сохранения информации в файл"""
        with open(self.filename, "w") as file:
            json.dump(vacancies, file, indent=2)

    def delete_vacancy(self):
        pass
