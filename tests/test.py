# coding=utf-8
import unittest

from tests.selenium_helpers.page_objects import *
from tests.selenium_helpers.constants import *
from selenium.webdriver import DesiredCapabilities, Remote


class Test(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test_log_in(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()

        self.assertEqual(USERNAME, email)

    def test_create_simple_adv(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.base_settings.set_product_type()
        create_page.base_settings.set_campaign_name(CAMP_NAME)
        create_page.base_settings.set_pads_targeting()
        create_page.create_advert.set_headline(HEADLINE)
        create_page.create_advert.set_text(TEXT)
        create_page.create_advert.set_url(URL)
        create_page.create_advert.set_image(os.path.abspath(IMAGE_NAME))
        create_page.create_advert.wait_picture()
        create_page.create_advert.submit()

        create_page.submit_button.submit()

        campaign_page = CampaignPage(self.driver)
        campaign_name = campaign_page.base_data.get_campaign_name()
        sex = campaign_page.base_data.get_sex()

        campaign_page.came_to_edit.click_edit_button()
        edit_page = EditPage(self.driver)
        headline = edit_page.data_from_edit.get_headline()
        text = edit_page.data_from_edit.get_text()
        edit_page.submit_button.submit()

        campaign_page_new = CampaignPage(self.driver)
        campaign_page_new.delete.click_delete_button()

        self.assertEqual(CAMP_NAME, campaign_name)
        self.assertEqual(TEXT, text)
        self.assertEqual(HEADLINE, headline)
        self.assertEqual(u'М и Ж', sex)

    def test_create_set_sex(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.base_settings.set_product_type()
        create_page.base_settings.set_campaign_name(CAMP_NAME)
        create_page.base_settings.set_pads_targeting()

        create_page.all_settings.set_sex()

        create_page.create_advert.set_headline(HEADLINE)
        create_page.create_advert.set_text(TEXT)
        create_page.create_advert.set_url(URL)
        create_page.create_advert.set_image(os.path.abspath(IMAGE_NAME))
        create_page.create_advert.wait_picture()
        create_page.create_advert.submit()

        create_page.all_settings.set_sex_M()

        create_page.submit_button.submit()

        campaign_page = CampaignPage(self.driver)
        sex = campaign_page.base_data.get_sex()
        campaign_page.delete.click_delete_button()

        self.assertEqual(u'Ж', sex)

    def test_create_set_interests(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.base_settings.set_product_type()
        create_page.base_settings.set_campaign_name(CAMP_NAME)
        create_page.base_settings.set_pads_targeting()

        create_page.all_settings.see_list_of_interests()
        create_page.all_settings.see_list_of_interests_proff()

        create_page.create_advert.set_headline(HEADLINE)
        create_page.create_advert.set_text(TEXT)
        create_page.create_advert.set_url(URL)
        create_page.create_advert.set_image(os.path.abspath(IMAGE_NAME))
        create_page.create_advert.wait_picture()
        create_page.create_advert.submit()

        create_page.all_settings.set_int_IT()
        create_page.all_settings.set_int_security()
        create_page.submit_button.submit()

        campaign_page = CampaignPage(self.driver)
        campaign_page.came_to_edit.click_edit_button()
        edit_page = EditPage(self.driver)
        edit_page.data_from_edit.see_list_of_interests()
        interests = edit_page.data_from_edit.get_interests()
        edit_page.submit_button.submit()

        campaign_page_new = CampaignPage(self.driver)
        campaign_page_new.delete.click_delete_button()

        self.assertEqual(u'IT/Интернет/Телеком', interests[0])
        self.assertEqual(u'Безопасность', interests[1])
        self.assertEqual(2, len(interests))

    def test_edit_sex(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.base_settings.set_product_type()
        create_page.base_settings.set_campaign_name(CAMP_NAME)
        create_page.base_settings.set_pads_targeting()

        create_page.all_settings.set_sex()

        create_page.create_advert.set_headline(HEADLINE)
        create_page.create_advert.set_text(TEXT)
        create_page.create_advert.set_url(URL)
        create_page.create_advert.set_image(os.path.abspath(IMAGE_NAME))
        create_page.create_advert.wait_picture()
        create_page.create_advert.submit()

        create_page.all_settings.set_sex_M()

        create_page.submit_button.submit()

        campaign_page = CampaignPage(self.driver)
        campaign_page.came_to_edit.click_edit_button()
        edit_page = EditPage(self.driver)
        edit_page.edit_data.set_sex()
        edit_page.edit_data.set_sex_M()
        edit_page.submit_button.submit()
        campaign_page_new = CampaignPage(self.driver)
        sex = campaign_page_new.base_data.get_sex()
        campaign_page_new.delete.click_delete_button()

        self.assertEqual(u'М и Ж', sex)

    def test_edit_interests(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()
        create_page.base_settings.set_product_type()
        create_page.base_settings.set_campaign_name(CAMP_NAME)
        create_page.base_settings.set_pads_targeting()

        create_page.all_settings.see_list_of_interests()
        create_page.all_settings.see_list_of_interests_proff()

        create_page.create_advert.set_headline(HEADLINE)
        create_page.create_advert.set_text(TEXT)
        create_page.create_advert.set_url(URL)
        create_page.create_advert.set_image(os.path.abspath(IMAGE_NAME))
        create_page.create_advert.wait_picture()
        create_page.create_advert.submit()

        create_page.all_settings.set_int_IT()
        create_page.all_settings.set_int_security()
        create_page.submit_button.submit()

        campaign_page = CampaignPage(self.driver)
        campaign_page.came_to_edit.click_edit_button()
        edit_page = EditPage(self.driver)
        edit_page.data_from_edit.see_list_of_interests()

        edit_page.edit_data.see_list_of_interests_proff()

        edit_page.edit_data.set_int_ALL()
        edit_page.submit_button.submit()

        campaign_page_new = CampaignPage(self.driver)
        campaign_page_new.came_to_edit.click_edit_button()

        edit_page_1 = EditPage(self.driver)
        edit_page_1.data_from_edit.see_list_of_interests()
        interests = edit_page_1.data_from_edit.get_interests()

        campaign_page_last = CampaignPage(self.driver)
        campaign_page_last.open()
        campaign_page_last.delete.click_delete_button()

        self.assertEqual(u'Профессиональная область', interests[0])
        self.assertEqual(1, len(interests))
