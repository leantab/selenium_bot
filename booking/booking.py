import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Booking(webdriver.Chrome):
    def __init__(self, driver_location='', teardown=False):
        # self.driver_location = driver_location
        os.environ['PATH'] += driver_location
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, *args):
        if self.teardown:
            self.quit()
            return super().__exit__(*args)

    def land_first_page(self):
        self.get(const.BASE_URL)

    def wait_for_text(self, element, text):
        WebDriverWait(self, 15).until(
            EC.text_to_be_present_in_element(
                element, 
                text
            )
        )