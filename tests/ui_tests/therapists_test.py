import allure
from allure_commons.types import Severity

from pages.therapists_page import therapists


class TestTherapistsPage:

    # @allure.label('owner', 'Ivanov Rostislav')
    # @allure.feature('Проверка работы страницы therapists')
    # @allure.tag('web')
    # @allure.severity(Severity.NORMAL)
    # def test_filters_should_has_short_filters(self):
    #     (therapists
    #      .open()
    #      .filters_should_be_not_selected())

    @allure.label('owner', 'Ivanov Rostislav')
    @allure.feature('Проверка работы страницы therapists')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    def test_header_links_should_be_clickable(self):
        (therapists.open()
         .links_should_be_clickable_header())

    @allure.label('owner', 'Ivanov Rostislav')
    @allure.feature('Проверка работы страницы therapists')
    @allure.tag('web')
    @allure.severity(Severity.BLOCKER)
    def test_psychologist_cards_should_increase(self):
        (therapists.open()
         .therapists_cards_should_increase())

    @allure.label('owner', 'Ivanov Rostislav')
    @allure.feature('Проверка работы страницы therapists')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    def test_sorting_for_max_price(self):
        (therapists.open()
         .choose_max_filter()
         .check_max_price_in_card())

    # @allure.label('owner', 'Ivanov Rostislav')
    # @allure.feature('Проверка работы страницы therapists')
    # @allure.tag('web')
    # @allure.severity(Severity.CRITICAL)
    # def test_compare_price_popup_and_card(self):
    #     (therapists.open()
    #      .click_info_icon_in_card()
    #      .check_price_in_info_popup())
    #
    # @allure.label('owner', 'Ivanov Rostislav')
    # @allure.feature('Проверка работы страницы therapists')
    # @allure.tag('web')
    # @allure.severity(Severity.NORMAL)
    # def test_choose_couple_therapy(self):
    #     (therapists.open()
    #      .choose_couple_therapy()
    #      .check_couple_symptoms_in_popup()
    #      .check_couple_therapy_short_filters())
    #
    # @allure.label('owner', 'Ivanov Rostislav')
    # @allure.feature('Проверка работы страницы therapists')
    # @allure.tag('web')
    # @allure.severity(Severity.MINOR)
    # def test_footer_should_have_links(self):
    #     (therapists.open()
    #      .check_footer_page_for_links())
