from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be

class IntroPage:

    def update_text(self):
        return browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Приложение устарело"]'))

    def skip_update(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.Button')).second.click()

    def button_continue(self):
        return browser.element((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Далее"]'))

    def button_start(self):
        return browser.element((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Начать"]'))

    def skip_intro_button(self):
        with step(f'Кнопка пропустить интро на стартовом экране есть'):
            return browser.element((AppiumBy.XPATH, f'//android.widget.Button[@content-desc="Пропустить"]'))

    def skip_intro(self):
        with step(f'Кнопка пропуск интро на стартовом экране нажата'):
            browser.element((AppiumBy.XPATH, f'//android.widget.Button[@content-desc="Пропустить"]')).click()

    def check_first_intro_page(self):
        with step("Проверка первой интро страницы"):
            self.skip_intro_button().should(be.not_.present)
            self.button_continue().should(be.clickable)
            self.screen_with_text()
            self.button_continue().click()

    def screen_with_text(self):
        with step("Проверка, что экран с интро текстом отображается"):
            return browser.element((AppiumBy.CLASS_NAME, "android.widget.ImageView")).should(be.visible)

    def check_second_intro_page(self):
        with step("Проверка второй интро страницы"):
            self.skip_intro_button().should(be.clickable)
            self.button_continue().should(be.clickable)
            self.screen_with_text()
            self.button_continue().click()

    def check_third_intro_page(self):
        with step("Проверка третьей интро страницы"):
            self.skip_intro_button().should(be.clickable)
            self.button_continue().should(be.clickable)
            self.screen_with_text()
            self.button_continue().click()

    def check_fourth_intro_page(self):
        with step("Проверка четвертой интро страницы"):
            self.skip_intro_button().should(be.clickable)
            self.button_continue().should(be.clickable)
            self.screen_with_text()
            self.button_continue().click()

    def check_fifth_intro_page(self):
        with step("Проверка пятой интро страницы"):
            self.screen_with_text()
            self.button_start().should(be.visible).should(be.clickable)
            self.button_start().click()

    def push_notification_screen(self):
        with step("На экране отображается настройка пуш-уведомлений"):
            return browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Включите уведомления"]'))

    def decline_notification(self):
        with step("Отмена включения пуш-уведомлений"):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Не сейчас"]')).click()

    def text_at_registration_screen(self):
        with step("Пользователю отображаются инпута кода страны и выбор страны на экране регистрации"):
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Россия"]')).should(be.visible)
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="+7"]')).should(be.visible)
            browser.element((AppiumBy.XPATH, '//android.widget.EditText')).should(be.visible)

    def check_text_at_registration_page_number(self):
        with step("Проверка текста над инпутом"):
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Создайте аккаунт\nв Ясно или войдите"]')
                            ).should(be.visible)
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Укажите номер телефона, который можно\n'
                                             'подтвердить с помощью SMS"]')).should(be.visible)

    def check_registration_page_through_number(self):
        self.skip_intro()
        with step("Проверка элементов на экране регистрации через мобильный номер"):
            self.check_text_at_registration_page_number()
            self.text_at_registration_screen()

    def go_to_email_registration_page_from_number_page(self):
        with step("Переход на с экрана регистрации по номеру телефона на экран регистрации по эмейлу"):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Вход по почте"]')).click()

    def check_registration_page_through_email(self):
        self.skip_intro()
        with step("Проверка кнопки входа по почте и переход на форму входа по почте"):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Вход по почте"]')).click()
        with step("Проверка текста над инпутом"):
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Вход по почте"]')).should(be.visible)
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Отправим код подтверждения. '
                                             'Только для зарегистрированных клиентов."]')).should(be.visible)
        with step("Проверка наличия поля ввода эмейла"):
            browser.element((AppiumBy.XPATH, "//android.widget.EditText")).click()
        with step("Появление кнопки 'Получить код'"):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Получить код"]')
                            ).should(be.visible).should(be.not_.disabled)

    def choose_another_country_for_number(self):
        self.skip_intro()
        with step("Клик по полю с выбором страны"):
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Россия"]')).click()
        with step("Открылся экран с выбором стран"):
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Код страны"]')).should(be.visible)
        with step("Выбрана страна Армения"):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Армения\n+374"]')).click()
        self.check_text_at_registration_page_number()
        with step("В качестве страны выбрана Армения"):
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Армения"]')).should(be.visible)
            browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="+374"]')).should(be.visible)

    def check_text_at_notification_page(self):
        return browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Включите уведомления"]')).should(be.visible)

    def user_can_walkthrough_intro(self):
        self.check_first_intro_page()
        self.check_second_intro_page()
        self.check_third_intro_page()
        self.check_fourth_intro_page()
        self.check_fifth_intro_page()
        self.text_at_registration_screen()
        
page_intro = IntroPage()