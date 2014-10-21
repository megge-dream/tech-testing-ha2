import os
import urlparse

from tests.selenium_helpers.components import *


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def base_settings(self):
        return BaseSettings(self.driver)

    @property
    def create_advert(self):
        return CreateAdvert(self.driver)

    @property
    def all_settings(self):
        return AllSettings(self.driver)

    @property
    def submit_button(self):
        return SubmitButton(self.driver)


class CampaignPage(Page):
    PATH = '/ads/campaigns/'

    @property
    def base_data(self):
        return BaseData(self.driver)

    @property
    def came_to_edit(self):
        return CameToEdit(self.driver)

    @property
    def delete(self):
        return DeleteButton(self.driver)


class EditPage(Page):
    @property
    def data_from_edit(self):
        return DataFromEdit(self.driver)

    @property
    def edit_data(self):
        return EditData(self.driver)

    @property
    def submit_button(self):
        return SubmitButton(self.driver)