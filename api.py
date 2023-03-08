import json

import requests


class RegRequest:
    def __init__(self):
        self.base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

    def get_api(self, params):
        """Эта функция принимает параметры GET-запроса
        и возвращает значение статус-кода и ответ json или text"""
        res = requests.get(self.base_url, params=params)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_api(self, params):
        """Эта функция для негативного тестирования. Она принимает параметры и выполняет
        POST-запрос. Возвращает значение статус-кода и ответ json или text"""
        res = requests.post(self.base_url, params=params)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_api(self, params):
        """Эта функция для негативного тестирования. Она принимает параметры и выполняет
        PUT-запрос. Возвращает значение статус-кода и ответ json или text"""
        res = requests.get(self.base_url, params=params)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def patch_api(self, params):
        """Эта функция для негативного тестирования. Она принимает параметры и выполняет
        PUTCH-запрос. Возвращает значение статус-кода и ответ json или text"""
        res = requests.get(self.base_url, params=params)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_api(self, params):
        """Эта функция для негативного тестирования. Она принимает параметры и выполняет
        DELETE-запрос. Возвращает значение статус-кода и ответ json или text"""
        res = requests.get(self.base_url, params=params)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
