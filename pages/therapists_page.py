from datetime import datetime
import allure
from selene import browser, be, by, have, query


class TherapistsPage:
    def __init__(self):
        self.therapists_cards = '.ysn-grid-without-outer-padding > div'
        self.short_filters = '[data-id="therapist-catalog-short-filters"]'
        self.apply_short_filters = '[data-id="therapist-catalog-short-filters"] ._flex-1'
        self.answers_to_questions = '._border-grey-500'
        self.price_of_therapists_in_card = '._items-center ._t-body-accent'
        self.price_of_therapists_in_popup = '._s-popup_content span'
        self.short_filters_popup = '._s-popup_layer'
        self.info_popup_about_therapist = '._mt-3 > ._tw-ui-icon'
        self.show_more = 'button._btn-base-secondary'
        self.symptoms = 'Симптомы'
        self.approach = 'Подход'
        self.price = 'Цена'
        self.gender = 'Пол'
        self.all_filters = 'Все фильтры'
        self.sort_short_filters = '[data-id="therapist-catalog-short-filters"] ._s-select._ml-auto'
        self.apply_filter_in_search_modal = '._s-popup_controls ._btn-base-primary'
        self.cancel_filter_in_search_modal = 'Отменить'
        self.clear_filter_in_search_modal = '._s-popup_controls ._btn-base-thetriary'
        self.enter_button = '.header__actions .nav-link'
        self.choose_psychologist_button = '.header__actions .header__btn'
        self.tests = 'Тесты'
        self.for_psychologists = 'Для психологов'
        self.for_business = 'Для бизнеса'
        self.gift_certificates = 'Подарочные сертификаты'
        self.main_header = '.header'

    @allure.step("Открытие страницы каталога терапевтов")
    def open(self):
        browser.open("/therapists")
        return self

    @allure.step("Проверка, что короткие фильтры отображаются на странице")
    def filters_should_be_not_selected(self):
        self.close_start_search_modal()
        browser.element(self.short_filters).should(be.visible)

    @allure.step("Разделы в хедере страницы кликабельны")
    def links_should_be_clickable_header(self):
        self.close_start_search_modal()
        browser.element(self.main_header).should(be.visible)
        browser.element(by.text(self.for_psychologists)).should(be.clickable)
        browser.element(by.text(self.for_business)).should(be.clickable)
        browser.element(by.text(self.gift_certificates)).should(be.clickable)
        browser.element(by.text(self.tests)).should(be.clickable)
        browser.element(self.enter_button).should(be.clickable)
        browser.element(self.choose_psychologist_button).should(be.clickable)

    @allure.step("Скролл страницы вниз к футеру")
    def scroll_to_footer_page(self):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        return self

    @allure.step("Скролл страницы вниз к футеру страницы")
    def scroll_page_down(self):
        browser.execute_script(f"window.scroll(0, 6000)")
        return self

    @allure.step("Нажатие кнопки 'Показать еще'")
    def press_button_show_more(self):
        browser.element(self.show_more).click()
        return self

    @allure.step("Количество карточек психологов увеличилось")
    def therapists_cards_should_increase(self):
        self.close_start_search_modal()
        len(browser.all(self.therapists_cards).should(have.size(25)))
        self.scroll_page_down()
        self.press_button_show_more()
        browser.execute_script(f"window.scroll(0, 1000)")
        browser.element(by.text('Ирина Ильина')).should(be.clickable)
        len(browser.all(self.therapists_cards).should(have.size(51)))

    @allure.step("Проверка футера на страницы на наличие ссылок для скачивания мобильного приложения")
    def check_footer_page_for_links(self):
        self.close_start_search_modal()
        self.scroll_to_footer_page()
        (browser.element('[src="https://assets.yasno.live/assets/'
                         'download-app-qr-code-a53314eca6f8cd49ac769031f5a28f92debaa2f0a9cb652ba21116c15149f12a.svg"]').
         should(be.clickable))
        browser.element("[aria-label='Скачать приложение Ясно в App Store']").should(be.clickable)
        browser.element("[aria-label='Скачать приложение Ясно в Google Play']").should(be.clickable)
        browser.element(by.text(f"© 2017–{datetime.now().year} Ясно")).should(be.visible)
        browser.element("[alt='Иконка Вконтакте']").should(be.clickable)
        browser.element("[alt='Иконка Яндекс дзен']").should(be.clickable)
        browser.element("[alt='Иконка Телеграм']").should(be.clickable)
        browser.element("[alt='Иконка Youtube']").should(be.clickable)
        browser.element("[alt='Иконка Сколково']").should(be.clickable)

    @allure.step("Выбор сортировке по максимальной цене")
    def choose_max_filter(self):
        self.close_start_search_modal()
        browser.element(self.sort_short_filters).click().element(by.text('Сначала дороже')).click()
        return self

    @allure.step("Цена в первой карточке 5150")
    def check_max_price_in_card(self):
        browser.element(self.price_of_therapists_in_card).should(have.exact_text('5150 ₽'))
        return self

    @allure.step("Закрытие стартовой модалки с поисковыми фильтрами")
    def close_start_search_modal(self):
        browser.element(by.text(self.cancel_filter_in_search_modal)).click()
        return self

    @allure.step('Клик по иконке доп.информации рядом в карточке терапевта')
    def click_info_icon_in_card(self):
        self.close_start_search_modal()
        browser.element(self.info_popup_about_therapist).click()
        return self

    @allure.step('Цена в попапе совпадает с ценой сессии терапевта')
    def check_price_in_info_popup(self):
        assert browser.element('._t-body-accent').get(
            query.text_content) == browser.element(self.price_of_therapists_in_popup).get(query.text_content)
        return self

    @allure.step('Выбор парной терапии')
    def choose_couple_therapy(self):
        browser.element(by.text('Парная')).click()
        return self

    @allure.step('Проверка, что в фильтрах отображаются парные симптомы')
    def check_couple_symptoms_in_popup(self):
        browser.element(self.short_filters_popup).element(by.text('Развод')).should(be.visible)
        browser.element(self.short_filters_popup).element(by.text('Созависимость')).should(be.visible)
        browser.element(self.apply_filter_in_search_modal).click()
        return self

    @allure.step('Проверка, что в фильтрах выбрана парная терапия')
    def check_couple_therapy_short_filters(self):
        browser.element(self.apply_short_filters).should(have.exact_text('Парная'))
        return self


therapists = TherapistsPage()
