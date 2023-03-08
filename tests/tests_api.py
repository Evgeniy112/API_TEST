import pytest

import settings
from api import RegRequest

tr = RegRequest()


@pytest.mark.api
class TestClassPos:

    @pytest.mark.get
    def test_get_api_sol(self, params=settings.valid_header_sol):
        # Позитивный тест GET-запроса фото марса по sol
        status, result = tr.get_api(params)
        photo = result['photos'][0]
        assert status == 200
        assert "photos" in result
        assert 'id' and 'sol' and 'camera' and 'img_src' and 'earth_date' and 'rover' in photo

    @pytest.mark.get
    def test_get_api_earth_date(self, params=settings.valid_header_earth_date):
        # Позитивный тест GET-запроса фото марса по earth_date
        status, result = tr.get_api(params)
        photo = result['photos'][0]
        assert status == 200
        assert "photos" in result
        assert 'id' and 'sol' and 'camera' and 'img_src' and 'earth_date' and 'rover' in photo


@pytest.mark.api
class TestClassNeg:

    @pytest.mark.get
    def test_get_api_sol_124(self, params=settings.invalid_header_sol_124):
        # Негативный тест GET-запроса фото марса по sol
        status, result = tr.get_api(params)
        assert status == 200
        assert "photos" in result

    @pytest.mark.get
    def test_get_api_earth_date_63(self, params=settings.invalid_header_earth_date_63):
        # Негативный тест GET-запроса фото марса по earth_date
        status, result = tr.get_api(params)
        assert status == 403
        assert "error" in result

    @pytest.mark.noget
    def test_post_api_274(self, params=settings.valid_header_earth_date):
        # Негативный тест запроса фото марса по earth_date
        # Указан метод POST вместо GET ТК №5 тестовые данные 274
        status, result = tr.post_api(params)
        assert status == 404
        assert "" in result
