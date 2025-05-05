from helpers.request import send_request, check_response_code
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.suite('api для каталога')
class TestCatalogAPI:
    stress_preset_ids = {"question_ids": [1, 2]}
    stress_preset_name = "Стресс"

    stress_preset_id = {
        "search_preset_id": 16
    }
    stress_preset_url = {
        "url_slug": "stress"
    }

    @allure.severity(Severity.BLOCKER)
    @allure.title('Количество психологов больше 0')
    def test_api_psychologist_count(self):
        response = send_request("/catalog/count", 'post', self.stress_preset_ids)

        assert response.json()["data"]["count"] > 0

        check_response_code(response, 200)

    @allure.severity(Severity.CRITICAL)
    @allure.title('Количество пресетов больше 0')
    def test_api_get_presets(self):
        response = send_request("/catalog/search_presets", 'get')

        assert len(response.json()["data"]["search_presets"]) > 0
        check_response_code(response, 200)

    @allure.severity(Severity.CRITICAL)
    @allure.title('Получении пресета по id')
    def test_api_get_by_presets(self):
        response = send_request("/catalog/by_search_preset", 'post', self.stress_preset_id)

        assert response.json()["data"]["search_preset"]["short_title"] == TestCatalogAPI.stress_preset_name
        check_response_code(response, 200)

    @allure.severity(Severity.NORMAL)
    @allure.title('Пресет "Стресс" существует')
    def test_api_get_preset(self):
        response = send_request("/catalog/search_preset", 'post', self.stress_preset_url)

        assert response.json()["data"]["search_preset"]["short_title"] == TestCatalogAPI.stress_preset_name
        check_response_code(response, 200)

    @allure.severity(Severity.NORMAL)
    @allure.title('Каталог возвращает список психологов')
    def test_api_get_catalog(self):
        response = send_request("/catalog", 'post', self.stress_preset_ids)
        check_response_code(response, 200)

        assert response.json()['data']['search_preset']['short_title'] == 'Все психологи'


    @allure.severity(Severity.NORMAL)
    @allure.title("Данные о психотерапевте")
    def test_api_get_therapist_info(self):
        response = send_request("/card/dk0F5ve4", 'get')
        check_response_code(response, 200)

        assert response.json()['data']['therapist']['fio'] == 'Анастасия Смирнова'
        assert response.json()['data']['therapist']['exp'] == 6