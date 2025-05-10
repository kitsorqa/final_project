from pages.yasno_pages.intro_page import page_intro

class TestIntroPage:
    def test_user_can_skip_intro(self):
        page_intro.skip_intro()

    def test_intro_walkthrough(self):
        page_intro.user_can_walkthrough_intro()

    def test_registration_page_number(self):
        page_intro.check_registration_page_through_number()

    def test_registration_page_email(self):
        page_intro.check_registration_page_through_email()

    def test_choose_another_country(self):
        page_intro.choose_another_country_for_number()