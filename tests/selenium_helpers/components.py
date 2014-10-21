# coding=utf-8
import os

from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.selenium_helpers.constants import *


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class BaseSettings(Component):
    CAMP_NAME = '.base-setting__campaign-name__input'
    PRODUCT_TYPE = '#product-type-5212'
    PADS_TARGET = '#pad-mm_groups_abstract'

    def set_campaign_name(self, campaign_name):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CAMP_NAME)
        )
        element.clear()
        element.send_keys(campaign_name)

    def set_product_type(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PRODUCT_TYPE)
        )
        element.click()

    def set_pads_targeting(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PADS_TARGET)
        )
        element.click()


class CreateAdvert(Component):
    HEADLINE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    URL = 'input[data-name="url"]'
    IMAGE = 'input[data-name="image"]'
    SAVE_BUTTON = '.banner-form__save-button'
    RESET_BUTTON = '.banner-form__reset'

    def set_headline(self, headline):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.HEADLINE)
        )
        element.send_keys(headline)

    def set_text(self, text):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TEXT)
        )
        element.send_keys(text)

    def set_url(self, url):
        self.url.send_keys(url)

    @property
    def url(self):
        elements = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_css_selector(self.URL)
        )
        for element in elements:
            if element.is_displayed():
                return element

    def set_image(self, image_path):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE)
        )
        element.send_keys(image_path)

    def loading_image(self, driver):
        images = driver.find_elements_by_css_selector('.banner-preview .banner-preview__img')
        for image in images:
            if image.value_of_css_property("width") == '90px':
                return WebDriverWait(image, 30, 0.1).until(
                    lambda d: d.value_of_css_property("background-image") is not None
                )

    def wait_picture(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.loading_image(d)
        )

    def submit(self):
        self.driver.find_element_by_css_selector(self.SAVE_BUTTON).click()

    def reset(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.RESET_BUTTON)
        )
        element.click()


class AllSettings(Component):
    SEX = '.campaign-setting__value'
    SEX_M = '#sex-M'
    SEX_F = '#sex-F'
    INTEREST = '.tree__node__input'
    INTEREST_ID_IT = '#interests238'
    INTEREST_ID_SEC = '#interests242'
    ALL_INTERESTS = "[data-node-id='interests']"
    ALL_PROFF_INTERESTS = '[data-node-id="Профессиональнаяобласть"]'

    def set_sex(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SEX)
        )
        element.click()

    def set_sex_M(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SEX_M)
        )
        element.click()

    def set_sex_F(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SEX_F)
        )
        element.click()

    def see_list_of_interests(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ALL_INTERESTS)
        )
        element.click()

    def see_list_of_interests_proff(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ALL_PROFF_INTERESTS)
        )
        element.click()

    def set_int_IT(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INTEREST_ID_SEC)
        )
        element = element.find_element_by_css_selector(self.INTEREST)
        element.click()

    def set_int_security(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INTEREST_ID_IT)
        )
        element = element.find_element_by_css_selector(self.INTEREST)
        element.click()


class SubmitButton(Component):
    SUBMIT_BUTTON = ".main-button-new"

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT_BUTTON).click()


class BaseData(Component):
    CAMP_NAME = '.campaign-title__name'
    SEX_STRING = '.campaign-title__settings'
    PADS_TARGET = '.campaign-settings-list__targeting__value .js-campaign-settings-value'

    def get_sex(self):
        base_string = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.SEX_STRING).text
        )
        sex_string = base_string.split(',')
        return sex_string[0]

    def get_campaign_name(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CAMP_NAME).text
        )

    def get_pads_targeting(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PADS_TARGET).text
        )

    def show_base_node(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SEX_STRING)
        )
        element.click()


class DataFromEdit(Component):
    INTERESTS_NAME = '.campaign-setting__chosen-box__item__name'
    ALL_INTERESTS = "[data-node-id='interests']"
    HEADLINE = '.banner-preview__title'
    TEXT = '.banner-preview__text'
    BLOCK = '.added-banner__banners-wrapper'

    def get_headline(self):
        block = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BLOCK)
        )
        return block.find_element_by_css_selector(self.HEADLINE).text

    def get_text(self):
        block = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BLOCK)
        )
        return block.find_element_by_css_selector(self.TEXT).text

    def get_interests(self):
        interests_names = []
        interests = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_css_selector(self.INTERESTS_NAME)
        )
        for interest in interests:
            interests_names.append(interest.text)
        return interests_names

    def see_list_of_interests(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.ALL_INTERESTS)
        )
        element.click()


class CameToEdit(Component):
    BUTTON = '.control__link_edit'

    def click_edit_button(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.BUTTON)
        )
        element.click()


class DeleteButton(Component):
    BUTTON = '.control__preset_delete'
    BLOCK = '.control_campaign'

    def click_delete_button(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BLOCK)
        )
        element.find_element_by_css_selector(self.BUTTON)
        element.click()


class EditData(Component):
    SEX = '.campaign-setting__value'
    SEX_M = '#sex-M'
    SEX_F = '#sex-F'
    INTEREST = '.tree__node__input'
    INTEREST_ID_IT = '#interests238'
    INTEREST_ID_ALL = '#interests237'
    INTEREST_ID_SEC = '#interests242'
    ALL_INTERESTS = "[data-node-id='interests']"
    ALL_PROFF_INTERESTS = '[data-node-id="Профессиональнаяобласть"]'

    def set_sex(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.SEX)
        )
        element.click()

    def set_sex_M(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SEX_M)
        )
        element.click()

    def set_sex_F(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SEX_F)
        )
        element.click()

    def see_list_of_interests(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.ALL_INTERESTS)
        )
        element.click()

    def see_list_of_interests_proff(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ALL_PROFF_INTERESTS)
        )
        element.click()

    def set_int_IT(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INTEREST_ID_SEC)
        )
        element = element.find_element_by_css_selector(self.INTEREST)
        element.click()

    def set_int_security(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INTEREST_ID_IT)
        )
        element = element.find_element_by_css_selector(self.INTEREST)
        element.click()

    def set_int_ALL(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INTEREST_ID_ALL)
        )
        element = element.find_element_by_css_selector(self.INTEREST)
        element.click()
