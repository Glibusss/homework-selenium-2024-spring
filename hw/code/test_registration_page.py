from base_case import BaseCase

class TestRegistrationPage(BaseCase):
    def test_element_rendering(self, registration_page):
        assert registration_page.header_became_visible()
        assert registration_page.create_new_cabinet_button_became_visible()
        assert registration_page.import_mytarget_cabinet_button_became_visible()