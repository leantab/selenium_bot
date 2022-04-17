from booking.booking import Booking
import booking.constants as const
import time

cities = const.CITIES

with Booking(teardown=True) as bot:
    bot.land_first_page()
    
    select = bot.find_element_by_id('form')
    options = select.find_elements_by_tag_name('option')
    time.sleep(2)
    for option in options:
        print(option.get_attribute('value') + ' => ' + option.text)
        option.click()
        time.sleep(1)

