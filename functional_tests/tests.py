from django contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys imort keys
from selenium.common.exceptions import WebDriverException

import time

MAX_WAIT = 10

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_item_in_html(self, the_element, the_text):
        start_time = time.time()
        while True:
            try:
                element = self.browser.find_element_by_id(the_element)
                self.assertIn(the_text, element)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_capturing_data_for_one_user(self):

        # The horsey community have heard of a smashing new online system
        # to track your horses fitness and condition.  Sandy goes to check out
        # the home page
        self.browser.get(self.live_server_url)

        # She is invited to enter her horses name
        horsename_input = self.browser.find_element_by_id('id_horse_name')
        self.assertEqual(
            horsename_input.get_attribute('placeholder'),
            'Enter Horse Name'
        )
        horsename_input.send_keys('Troy my Boy')
        # When she hits enter the page updates and her horses name is listed
        horsename_input.send_keys(Keys.ENTER)
        self.wait_for_item_in_html('horse_name', 'Troy my Boy')

        # She is invited to enter her horses weight
        # When she hits enter the page updates and her horses weight is listed

        # She is invited to enter her horses tape measurements
        # When she hits enter the page updates and her horses measurements are listed

        # The site generates a unique URL for her and her horse
